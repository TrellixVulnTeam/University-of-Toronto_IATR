package model;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.logging.FileHandler;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * The GoGoPhotoSystem program implements an application that sets up TagManager,
 * ImageManager, DirectoryManager and logger. It also give access to get the TagManager,
 * ImageManager and DirectoryManager by getter method.
 *
 * @see TagManager, ImageManager, DirectoryManager and LoggerManager
 */
public class GoGoPhotoSystem {
    /**
     * A TagManager that manages Tag objects
     *
     * @see TagManager
     */
    private TagManager tagManager ;

    /**
     * A ImageManager that manages Image objects
     *
     * @see ImageManager
     */
    private ImageManager imageManager;

    /**
     * Create a new logger to track the logging history.
     *
     * @see LoggerManager
     */
    public static Logger logger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    /**
     * Create a new DirectoryManager to operate and display the selected directory
     *
     * @see DirectoryManager
     */
    private DirectoryManager directoryManager = new DirectoryManager();

    /**
     * This method creates a new GoGoPhotoSystem with given tage and image  files' path.
     * @param tagFilePath a file path of storage file to read or create.
     * @param imageFilePath a file path of storage file to read or create.
     * @throws ClassNotFoundException
     * @throws IOException
     */
    public GoGoPhotoSystem (String tagFilePath, String imageFilePath) throws ClassNotFoundException, IOException {

        // Reads serializable objects from file.
        // Populates the record list using stored data, if it exists.
        File tagManagerFile = new File(tagFilePath);
        File imageManagerFile = new File(imageFilePath);


        imageManager = new ImageManager();
        tagManager =  new TagManager();
        imageManager.addObserver(tagManager);


        if (tagManagerFile.exists()) {
            readFromTagManagerFile(tagFilePath);
        } else {
            tagManagerFile.createNewFile();
        }

        if (imageManagerFile.exists()) {
            readFromImageManagerFile(imageFilePath);
        } else {
            imageManagerFile.createNewFile();
        }
        MyFormatter formatter = new MyFormatter();
        logger.setLevel(Level.ALL);
        Handler fileHandler = new FileHandler("LogHis.txt", true);
        fileHandler.setLevel(Level.ALL);
        logger.addHandler(fileHandler);
        fileHandler.setFormatter(formatter);


    }

    /**
     * Read the stored file based on the input file path and assign deserialize result to tagManager.tags.
     * @param path the path of the stored file
     * @throws ClassNotFoundException
     */
    public void readFromTagManagerFile(String path) throws ClassNotFoundException{
        try {
            InputStream file = new FileInputStream(path);
            InputStream buffer = new BufferedInputStream(file);
            ObjectInput input = new ObjectInputStream(buffer);

            //deserialize
            tagManager.tags = (HashMap<String, Integer>) input.readObject();
            input.close();
        } catch (IOException ex) {
            java.lang.System.out.println("Cannot read from input.");
        }
    }

    /**
     * Read the stored file based on the input file path and assign deserialize result to imageManager.images.
     * @param path
     * @throws ClassNotFoundException
     */
    public void readFromImageManagerFile(String path) throws ClassNotFoundException{
        try {
            InputStream file = new FileInputStream(path);
            InputStream buffer = new BufferedInputStream(file);
            ObjectInput input = new ObjectInputStream(buffer);

            //deserialize
            imageManager.images = (ArrayList<Image>) input.readObject();
            input.close();
        } catch (IOException ex) {
            java.lang.System.out.println("Cannot read from input.");
        }
    }


    /**
     * This method save the data to the input file path by calling saveToTagManagerFile method of tagManager.
     * @param filePath the path to the location that the data is stored
     * @see TagManager
     * @throws IOException
     */
    public void saveToTagManagerFile(String filePath) throws IOException{
        tagManager.saveToTagManagerFile(filePath);
    }


    /**
     * This method save the data to the input file path by calling saveToImageManagerFile method of imageManager.
     * @param filePath the path to the location that the data is stored
     * @see ImageManager
     * @throws IOException
     */
    public void saveToImageManagerFile(String filePath) throws IOException{
        imageManager.saveToImageManagerFile(filePath);
    }


    /**
     * Return the directoryManager.
     * @return the directoryManager that is returned
     */
    public DirectoryManager getDirectoryManager() {
        return directoryManager;
    }

    /**
     * Return the tagManager
     * @return the tagManager that is returned
     */
    public TagManager getTagManager() {
        return tagManager;
    }

    /**
     * Return the imageManager
     * @return the imageManager that is returned
     */
    public ImageManager getImageManager() {
        return imageManager;
    }

}