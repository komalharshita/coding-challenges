// ConstructorMethodDemo.java
class Book {
    private String title;
    private String author;

    // Constructor
    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    // Public method
    public void display() {
        System.out.println("Book: " + title + " by " + author);
    }

    // Private helper method
    private void secretNote() {
        System.out.println("This is a secret note inside the book!");
    }

    // Protected method
    protected void showProtected() {
        System.out.println("Protected access example for: " + title);
    }
}

public class ConstructorMethodDemo {
    public static void main(String[] args) {
        Book b1 = new Book("Java Basics", "John Doe");
        b1.display();
        b1.showProtected();
        // b1.secretNote();  // Not accessible
    }
}
