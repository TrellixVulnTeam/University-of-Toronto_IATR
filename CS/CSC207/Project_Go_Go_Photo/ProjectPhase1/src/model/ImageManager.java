package model;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.logging.Level;

import static java.nio.file.StandardCopyOption.REPLACE_EXISTING;
/**
 * This class is responsible for move a image to another directory,
 * rename an image, add tag to an image's name,
 * delete tag from an image's name(while keep the original suffix).
 * This class is also responsible for renaming an Image back to one of its used name.
 * Besides, it also serializes the ALL images in the arraylist of ImageManager.
 * This helps GUI to display all the images in the arraylist.
 */
public class ImageManager implements Serializable {
    public ArrayList<Image> images;

    /**
     * Initialize ImageManager object, meanwhile, creating an Arraylist that is used
     * to hold images.
     */
    public ImageManager(){
        this.images = new ArrayList<>();
    }

    /**
     * Adds an image to the ArrayList of ImageManager.
     * @param picture the picture to be added to the ArrayList
     */
    public void addImage(Image picture){
        this.images.add(picture);
    }

    /**
     * Gets the Image object given a file path. returns null if the image object
     * doesn't exist.
     *
     * @param path the path given to find the Image object.
     * @return the Image object given a file path. returns null if the image object
     * cannot be found
     */
    public Image foundImage(String path){
        for (int i=0; i<this.images.size(); i++){
            if (this.images.get(i).getPath().toString().equals(path)){
                return this.images.get(i);
            }
        }
        return null;
    }

    /**
     *
     * @param image
     * @param newName
     */
    protected void renameFile(Image image, String newName){
        String oldPath = image.getPath().toString();
        String newPath = oldPath.substring(0, oldPath.lastIndexOf(File.separator));
        newPath = newPath + File.separator + newName + "." + image.getType();

        File oldFile = new File(image.getPath().toString());

        image.setName(newName);
        image.setPath(newPath);
        image.addNewNameToHistory(newName);
        File newFile = new File(newPath);
        oldFile.renameTo(newFile);

    }

    /**
     *
     * @param image
     * @param new_path
     * @throws IOException
     */
    public void moveImageToDirectory(Image image, String new_path) throws IOException {
        String newImagePath = new_path + File.separator + image.getName() + "." + image.getType();
        Files.move(Paths.get(image.getPath()), Paths.get(newImagePath), REPLACE_EXISTING);
        image.setPath(newImagePath);
    }

    /**
     *
     * @param image
     * @param name
     */
    public void backToOldName(Image image, String name){
        String oldName = name.substring(0, name.lastIndexOf("."));
        String curName = image.getName();
        ArrayList<String> tagsList = image.getTags();
        renameFile(image, oldName);
        String[] nameTags = oldName.split(" @");
        ArrayList<String> tagContainer = new ArrayList<>();
        for (int i=1; i<nameTags.length; i++){
            tagContainer.add(nameTags[i]);
        }
        image.resetTags(tagContainer);
        for (int i=0; i< tagsList.size(); i++){
            if (! image.getTags().contains(tagsList.get(i))){
                image.notifyDown(tagsList.get(i));
            }
        }
        for (int i=0; i< image.getTags().size(); i++){
            if (! tagsList.contains(image.getTags().get(i))){
                image.notifyUp(image.getTags().get(i));
            }
        }
        GoGoPhotoSystem.logger.log(Level.FINE,"Changes from current name: "+curName+", to new name: "+image.getFullName());
    }

    /**
     *
     * @param image
     * @param tag
     * @return
     */
    public boolean deleteTagFromName(Image image, String tag){
        if (! image.getTags().contains(tag)){
            return false;
        } else {
            String[] nameParts = image.getName().split(" @");
            StringBuilder newFileName = new StringBuilder();
            newFileName.append(nameParts[0]);
            for (int i=1; i<nameParts.length; i++){
                if (!nameParts[i].equals(tag)){
                    newFileName.append(" @");
                    newFileName.append(nameParts[i]);
                }
            }
            String oldName = image.getFullName();
            this.renameFile(image, newFileName.toString());
            image.deleteTags(tag);
            GoGoPhotoSystem.logger.log(Level.FINE,"Old Name: "+ oldName + ", New Name: "+image.getFullName());
            return true;
        }
    }

    /**
     * Adds a tag to the given image. It
     * @param image The image to be added tag on
     * @param tagName the tag to be added on
     * @return
     */
    public void addTagToName(Image image, String tagName){
        String oldName = image.getFullName();
        String newFileName = image.getName() + " @" + tagName;
        this.renameFile(image, newFileName);
        image.addTags(tagName);
        GoGoPhotoSystem.logger.log(Level.FINE,"Old Name: "+ oldName + ", New Name"+image.getFullName());
    }

    /**
     * Saves the images(the arraylist of images in the ImageManager) to the given filePath
     * @param filePath saves the image to the given path
     * @throws IOException
     */
    public void saveToImageManagerFile(String filePath) throws IOException{
        OutputStream file = new FileOutputStream(filePath);
        OutputStream buffer = new BufferedOutputStream(file);
        ObjectOutput output = new ObjectOutputStream(buffer);

        // serialize the imageManager
        output.writeObject(images);
        output.close();
    }



    /**
     * Returns whether the given image's tags include the newTag.
     * @param image the image to be checked whether it has the given newTag
     * @param newTag the tag to be check whether the image has
     * @return returns true if the given image's tags include the newTag.
     */
    public boolean foundTag(Image image, String newTag) {
        for (Tag t : image.getTagList()) {
            if (t.getName().equals("@" + newTag)) {
                return true;
            }
        }
        return false;
    }
}
