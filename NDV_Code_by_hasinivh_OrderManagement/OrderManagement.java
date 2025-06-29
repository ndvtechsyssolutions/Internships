import org.hibernate.*;
import org.hibernate.cfg.Configuration;

import jakarta.persistence.*;

@Entity
class Customer {
    @Id
    @GeneratedValue
    private int id;
    private String name;

    public Customer() {}
    public Customer(String name) { this.name = name; }

    public int getId() { return id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}

public class SimpleOrderApp {
    public static void main(String[] args) {
        // Hibernate config
        Configuration cfg = new Configuration();
        cfg.setProperty("hibernate.connection.driver_class", "com.mysql.cj.jdbc.Driver");
        cfg.setProperty("hibernate.connection.url", "jdbc:mysql://localhost:3306/orderdb");
        cfg.setProperty("hibernate.connection.username", "root");
        cfg.setProperty("hibernate.connection.password", "your_password"); // <-- Change this
        cfg.setProperty("hibernate.dialect", "org.hibernate.dialect.MySQLDialect");
        cfg.setProperty("hibernate.hbm2ddl.auto", "update");
        cfg.setProperty("hibernate.show_sql", "true");

        cfg.addAnnotatedClass(Customer.class);

        SessionFactory factory = cfg.buildSessionFactory();
        Session session = factory.openSession();
        Transaction tx = session.beginTransaction();

        Customer customer = new Customer("Honey");
        session.save(customer);

        tx.commit();
        session.close();
        factory.close();

        System.out.println("✔ Customer saved to DB!");
    }
}
