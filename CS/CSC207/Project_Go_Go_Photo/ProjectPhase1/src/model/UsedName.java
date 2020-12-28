package model;

import java.io.Serializable;

/**
 * This class is used to display every used name of an Image via GUI.
 */
public class UsedName implements Serializable {
    private String name;

    /**
     * The contructor of an UsedName object includes the name of the used name.
     * @param name
     */
    public UsedName(String name){
        this.name = name;
    }

    /**
     * Gets the used name's name.
     *
     * @return the name of an used name of an image.
     */
    public String getName() {
        return this.name;
    }
}
