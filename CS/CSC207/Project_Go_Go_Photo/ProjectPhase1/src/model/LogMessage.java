package model;

/**
 * <h1>Generate an object to represent a log message with time and content</h1>
 * The LogMessage program implements an application that
 * generate a LogMessage object with time and content
 * (which is the current name of a operated image
 * accorded into log history(LogHis.txt))of this LogMessage
 *
 * @see LoggerManager
 */
public class LogMessage {

    /**
     * The time of this LogMessage
     */
    private String time;

    /**
     * The content of this LogMessage
     */
    private String content;

    /**
     * This method create a new LogMessage with given
     * time and content of this LogMessage.
     * @param time the time of this LogMessage
     * @param content the content of this log message, which
     *                is the the current name of a operated image
     */
    public LogMessage(String time, String content){
        this.time = time;
        this.content = content;
    }

    /**
     * Convert this LogMessage into a readable string
     * @return A string with the time and the content
     * of this LogMessage
     */
    @Override
    public String toString() {
        return time + content;
    }

    /**
     * Gets the time of this LogMessage.
     * @return the time of this LogMessage
     */
    public String getTime(){return this.time;}

    /**
     * Gets the content of this LogMessage.
     * @return the content of this LogMessage
     */
    public String getContent(){return this.content;}

}
