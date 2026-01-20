---
type: link
source: notion
url: https://aws.amazon.com/blogs/database/dynamic-view-based-data-masking-in-amazon-rds-and-amazon-aurora-mysql/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-09-19T04:14:00.000Z
---

# Dynamic view-based data masking in Amazon RDS and Amazon Aurora MySQL | Amazon Web Services

## Overview (from Notion)
- Data masking is crucial for protecting sensitive information, which is increasingly important in your role as a software engineer and founder, especially given the heightened focus on data privacy regulations.
- The dynamic view-based approach allows for real-time data protection without compromising the usability of the data for development or analytics, reflecting a balance between security and functionality.
- This method can enhance your company's reputation by showing clients that you take data privacy seriously, potentially giving you a competitive edge in the market.
- Implementing this solution could save time and resources by automating the masking process, freeing you to focus on innovation and growth.
- Consider the potential for future scalability; as your company grows, so will the need for more sophisticated data handling techniques.
- An alternate view might be that relying on automated masking solutions could introduce risks if not regularly maintained or audited for effectiveness.
- The ability to customize masking types and configurations means you can tailor solutions to fit specific project needs, enhancing your adaptability in an ever-evolving tech landscape.

## AI Summary (from Notion)
Data masking is crucial for protecting sensitive information while allowing its use in development and analytics. Amazon RDS and Aurora MySQL lack native data masking features, but a view-based approach can be implemented to mask sensitive data dynamically. This involves creating configuration tables, stored procedures, and views that allow different user access levels to masked data, ensuring real-time data protection without duplicating data. The solution is flexible but requires manual updates for schema changes and may impact performance.

## Content (from Notion)

Data masking is an important technique in cybersecurity, allowing organizations to safeguard personally identifiable information (PII) and other confidential data, while maintaining its utility for development, testing, and analytics purposes. Data masking involves replacing original sensitive data with false, yet realistic information. This process helps ensure that the masked version preserves the format and characteristics of the original data, making it indistinguishable from real data for most purposes, while eliminating the risk of exposing actual sensitive details.

In MySQL community versions, there are no built-in data masking abilities. By extension, Amazon Relational Database Service (Amazon RDS) for MySQL and Amazon Aurora MySQL-Compatible Edition also do not have a native data masking feature today. However, while there are no native data masking abilities, you can leverage view-based data masking to create database views to hide or transform sensitive data, while preserving the original information. In this post, we show you a step-by-step solution for implementing view-based data masking in Amazon RDS and Aurora MySQL.

## Solution overview

The solution uses view-based masking capabilities in Amazon RDS for MySQL and Aurora MySQL-Compatible Edition to implement role-based access control for sensitive data. Using example tables (employees, customers, and patients), we demonstrate how to create and manage database views that automatically mask sensitive fields such as Social Security numbers and email addresses. Through these views, administrative users can maintain complete data visibility into the original table, while other users are denied access to the original table and can only access masked versions of the sensitive data through views. This view-based masking approach not only provides robust data protection, but also offers a maintainable and scalable solution for managing data access across your organization. The following diagram shows the steps involved in the MySQL custom data masking solution:

As shown in the preceding figure, the following actions take place:

1. The administrator inserts the desired columns and subsequent tables to be masked into the configuration table named data_mask_configuration.
1. The administrator calls a stored procedure to generate a masked view of the tables using the metadata entered in the configuration table.
1. The stored procedure creates a masked view of the table/s.
1. The developer can access the masked view of the table/s without revealing any sensitive data.
It’s important to note that this solution is designed to work with live, dynamic environments. The views created are not static snapshots, but rather live representations of the source tables, automatically reflecting any changes made to the underlying data. Any changes to table structure/schema would require a few extra steps. We discuss this later in the post in the Pros, Cons, and Customization section.

By creating a masked view within the same database, it allows for real-time data analysis by users who need current data, but shouldn’t have access to sensitive information. It’s also useful for debugging production issues where sanitized, up-to-date data is necessary. This solution provides flexibility to address various data access scenarios while maintaining data protection.

## Prerequisites

To follow along, you must have an RDS or Aurora MySQL database which you can connect. Within this database, you must be able to create the configuration table, a data masking function, and a stored procedure to perform the data masking. This requires the following access and privileges:

- Full access to the configuration table
- CREATE FUNCTION privilege
- CREATE PROCEDURE privilege
## Create the configuration table

First, you need to create a table to track which columns in which tables contain PII. You’ll use the mask_type column and the ENUM data type for the different levels of data masking in the database. These values include FULL for complete data masking, PARTIAL for partial data masking, EMAIL for specific masking for email addresses, and NONE for no masking applied. These options can be customized to fit your use case in the Create the masking function section.

1. Create a database where the configuration table will exist if you haven’t already: 
1. And then use this database: 
1. Next, create the configuration table (data_mask_configuration) to track which columns you want to mask across your database: 
## Create the masking function

You now create the masking function that’s responsible for masking the data when you create a view of the table. The type of masking performed depends on what values are inserted into the data_mask_configuration table that you created.

Create the masking function:

```plain text
DELIMITER //
CREATE FUNCTION get_masked_column_error_handling(p_schema VARCHAR(64), p_table VARCHAR(64), p_column VARCHAR(64))
RETURNS TEXT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_mask_type ENUM('FULL', 'PARTIAL', 'EMAIL', 'NONE');
    DECLARE v_found INT DEFAULT 0;

    -- Error handler for SQL exceptions
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error in get_masked_column function';
    END;

    -- Input validation
    IF p_schema IS NULL OR p_table IS NULL OR p_column IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Parameters cannot be null';
    END IF;

    -- Get mask type and check if row exists
    SELECT mask_type, 1 INTO v_mask_type, v_found
    FROM data_mask_configuration
    WHERE table_schema = p_schema
    AND table_name = p_table
    AND column_name = p_column
    LIMIT 1;

    -- If no matching row found, set to NONE
    IF v_found = 0 THEN
        SET v_mask_type = 'NONE';
    END IF;
    CASE v_mask_type
        WHEN 'FULL' THEN RETURN CONCAT('''XXXXX'' AS ', p_column);
        WHEN 'PARTIAL' THEN RETURN CONCAT('CONCAT(LEFT(', p_column, ', 2), ''***'') AS ', p_column);
        WHEN 'EMAIL' THEN RETURN CONCAT('CONCAT(LEFT(', p_column, ', 1), ''***@'', SUBSTRING_INDEX(', p_column, ', ''@'', -1)) AS ', p_column);
        ELSE RETURN p_column;
    END CASE;
END //
DELIMITER ;
```

The PARTIAL and EMAIL masking types can be customized based on your use case.

## Create stored procedures to generate masked views

Now, you create two stored procedures for later use. These procedures will generate masked views for the tables. In this example, you create two procedures:

- generate_masked_view: Used to create a masked view for a specific table.
- generate_all_masked_views: Used to create masked views for all tables included within the data_mask_configuration table.
When setting up the procedure for a specific table, you can select which table you want to make the view for.

In these examples, we use masked_ as the prefix of the view name. You can change this view name format to suit your use case.

Stored procedure for a specific table:

```plain text
DELIMITER //
CREATE PROCEDURE generate_masked_view(IN p_schema VARCHAR(64), IN p_table VARCHAR(64))
BEGIN
    DECLARE v_columns TEXT;
    DECLARE v_sql TEXT;
    SELECT GROUP_CONCAT(
        CASE
            WHEN pc.mask_type IS NOT NULL THEN get_masked_column(p_schema, p_table, c.COLUMN_NAME)
            ELSE c.COLUMN_NAME
        END
    )
    INTO v_columns
    FROM INFORMATION_SCHEMA.COLUMNS c
    LEFT JOIN data_mask_configuration pc ON pc.table_schema = c.TABLE_SCHEMA
                             AND pc.table_name = c.TABLE_NAME
                             AND pc.column_name = c.COLUMN_NAME
    WHERE c.TABLE_SCHEMA = p_schema AND c.TABLE_NAME = p_table;
    SET @sql = CONCAT('CREATE OR REPLACE VIEW ', p_schema, '.masked_', p_table, ' AS SELECT ', v_columns, ' FROM ', p_schema, '.', p_table);
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //
DELIMITER ;
```

Stored procedure for all tables:

```plain text
DELIMITER //
CREATE PROCEDURE generate_all_masked_views()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_schema, v_table VARCHAR(64);
    DECLARE cur CURSOR FOR
        SELECT DISTINCT table_schema, table_name
        FROM data_mask_configuration;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_schema, v_table;
        IF done THEN
            LEAVE read_loop;
        END IF;
        CALL generate_masked_view(v_schema, v_table);
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;
```

## Insert columns to mask within the configuration table

Now, you can insert columns with data that you want masked into the configuration table. This example uses the demo tables employees, customers, and patients which exist within the mydb schema.

Below are examples of rows we inserted into the data_mask_configuration table:

```plain text
('mydb', 'employees', 'ssn', 'FULL'),
('mydb', 'employees', 'email', 'EMAIL'),
('mydb', 'customers', 'credit_card', 'FULL'),
('mydb', 'customers', 'phone', 'PARTIAL'),
('mydb', 'customers', 'email', 'EMAIL'),
('mydb', 'patients', 'medical_record_num', 'FULL'),
('mydb', 'patients', 'dob', 'FULL'),
('mydb', 'patients', 'insurance_id', 'FULL');
```

Note: If a developer wants to add additional masked columns, they must have SELECT, INSERT, and UPDATE permissions to the configuration Table.

## Create masked views for tables

In this section, you call the stored procedures to generate the masked views. When the stored procedure generates the views, it can result in greater CPU utilization depending on the size of the table because the tables are masked on the fly. Generating the masked views concurrently can also result in increased CPU utilization.

Call the stored procedure for a specific table (for example, the employees table in the mydb schema):

```plain text
CALL generate_masked_view('mydb','employees');
```

Call the stored procedure for all tables:

```plain text
CALL generate_all_masked_views();
```

High I/O activity can occur when calling the stored procedure generate_all_masked_views(), because it recreates the views for all entries in the data_mask_configuration table.

## Test the solution

After creating the masked views as the administrator user, you can create a new user and restrict it to access only the masked view in order to simulate what a developer would observe.

1. Create a new user 
1. Only provide this user with the ability to view the masked views 
1. Use this same user and attempt to read from the newly created masked views 
## Considerations for maintaining the solution

In this section, we provide the create script for two stored procedures. One that you can use to quickly update the mask type of a specific row within the data_mask_configuration table. You can use the other stored procedure to insert columns into the data_mask_configuration table.

Stored procedure: Update the mask type of a specific row

```plain text
DELIMITER //
CREATE PROCEDURE update_pii_mask_type(
    IN p_schema VARCHAR(64),
    IN p_table VARCHAR(64),
    IN p_column VARCHAR(64),
    IN p_new_mask_type VARCHAR(20)
)
BEGIN
    UPDATE data_mask_configuration
    SET mask_type = p_new_mask_type
    WHERE table_schema = p_schema
    AND table_name = p_table
    AND column_name = p_column;

    -- Optional: Regenerate the masked view for this table
    CALL generate_masked_view(p_schema, p_table);
END //
DELIMITER ;
```

This stored procedure is only for updating the mask type. DDL changes must be manually altered.

Stored procedure: Row insertion

```plain text
DELIMITER //
CREATE PROCEDURE insert_data_mask_configuration(
    IN p_schema VARCHAR(64),
    IN p_table VARCHAR(64),
    IN p_column VARCHAR(64),
    IN p_mask_type VARCHAR(20)
)
BEGIN
    INSERT INTO data_mask_configuration (table_schema, table_name, column_name, mask_type)
    VALUES (p_schema, p_table, p_column, p_mask_type);
END //
DELIMITER ;
```

An important consideration when you’re updating the data_mask_configuration table is that you must also recreate your views. If you perform UPDATE, DELETE, or INSERT operations within the data_mask_configuration table, your views will not be automatically updated. This is why it’s important to rerun either the generate_masked_view(‘db’,‘table’) or generate_all_masked_views() stored procedure. You can also build a trigger or different solution to automatically detect changes and regenerate the required view.

## Pros, Cons, and Customization

We now cover the pros and cons of this solution as well as how to best customize it in order to fit your business use case.

Pros:

1. Real-time data masking: The solution provides live, dynamic masking of sensitive data without creating separate copies.
1. Flexible and customizable: Can be adapted to various masking requirements and data types.
1. Role-based access control: Allows different levels of data access for different users.
1. No additional software required: Utilizes built-in MySQL features.
Cons:

1. Manual updates required: Changes to table structures necessitate manual updates to the configuration and view regeneration. If the table structure changes (such as new columns are added), you must update the data_mask_configuration table.
1. Performance impact: Creating the masked views can cause performance degradation depending on the amount of data to be masked and number of views created.
1. Maintenance overhead: Requires ongoing management of the masking configuration and views.
Customization considerations:

1. Masking Functions: Modify the get_masked_column_error_handling function to include additional masking types or alter existing ones to suit your specific data patterns.
1. Configuration Table: Extend the data_mask_configuration table to include additional metadata, such as reason for masking or last review date.
1. View Naming: Adjust the view naming convention in the generate_masked_view procedure to align with your organization’s naming standards.
1. Logging and Auditing: Add logging capabilities to track when and by whom masked data is accessed.
When implementing this solution, carefully consider these factors and adjust the approach as needed to meet your specific security requirements and operational needs. Regular review and testing of the masking implementation is crucial to ensure ongoing effectiveness and compliance with data protection standards.

## Clean up

If you no longer require the resources used to set up this configuration, delete the following resources to avoid incurring future charges:

1. To delete a DB instance, see Deleting a DB instance
1. To delete an Aurora cluster and its DB Instances, see Deleting Aurora DB clusters and DB instances
1. Drop the stored procedures 
1. Drop the function 
1. Drop the configuration table 
## Conclusion

In this post, we presented a view-based data masking solution you can use in your Aurora MySQL and RDS for MySQL databases. You can use this solution to meet your business and security requirements. Leave your feedback in the comments section.

### About the authors

Cade Kettner

Nirupam Datta

Ryan Moore


