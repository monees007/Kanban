import Dime;
public class Card {
    String title;
    content;
    Boolean flag_complete;
    date Deadline;
    list_parent;
    date date_created;

    public Card(String title, String content, date deadline, Clist parent) {
        this.title = title;
        this.content = content;
        this.flag_complete = false;
        this.Deadline = deadline;
        this.list_parent = parent;
        this.date_created= Dime.c_time;// Todo: implement date cearted,
    }
}
