# MySQL View-Based Data Masking

View-based data masking for Amazon RDS MySQL and Aurora MySQL to protect sensitive data (PII) while maintaining utility for development and analytics.

## Why View-Based Masking

- MySQL community edition (and thus RDS/Aurora MySQL) lacks native data masking
- Views provide live, dynamic masking without data duplication
- Role-based access: admins see original data, developers see masked views
- Real-time reflection of underlying data changes

## Architecture

1. **Configuration table** (`data_mask_configuration`) tracks which columns need masking
2. **Masking function** transforms data based on mask type
3. **Stored procedures** generate masked views from configuration
4. **Views** named with `masked_` prefix provide sanitized access

## Mask Types

```sql
ENUM('FULL', 'PARTIAL', 'EMAIL', 'NONE')
```

- **FULL**: Replace with 'XXXXX'
- **PARTIAL**: Show first 2 chars + '***' (e.g., "Jo***")
- **EMAIL**: First char + '***@' + domain (e.g., "j***@example.com")
- **NONE**: No masking

## Implementation Steps

### 1. Configuration Table

```sql
CREATE TABLE data_mask_configuration (
    table_schema VARCHAR(64),
    table_name VARCHAR(64),
    column_name VARCHAR(64),
    mask_type ENUM('FULL', 'PARTIAL', 'EMAIL', 'NONE')
);
```

### 2. Masking Function

```sql
CREATE FUNCTION get_masked_column_error_handling(
    p_schema VARCHAR(64),
    p_table VARCHAR(64),
    p_column VARCHAR(64)
)
RETURNS TEXT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_mask_type ENUM('FULL', 'PARTIAL', 'EMAIL', 'NONE');
    DECLARE v_found INT DEFAULT 0;

    SELECT mask_type, 1 INTO v_mask_type, v_found
    FROM data_mask_configuration
    WHERE table_schema = p_schema
    AND table_name = p_table
    AND column_name = p_column
    LIMIT 1;

    IF v_found = 0 THEN
        SET v_mask_type = 'NONE';
    END IF;

    CASE v_mask_type
        WHEN 'FULL' THEN RETURN CONCAT('''XXXXX'' AS ', p_column);
        WHEN 'PARTIAL' THEN RETURN CONCAT('CONCAT(LEFT(', p_column, ', 2), ''***'') AS ', p_column);
        WHEN 'EMAIL' THEN RETURN CONCAT('CONCAT(LEFT(', p_column, ', 1), ''***@'', SUBSTRING_INDEX(', p_column, ', ''@'', -1)) AS ', p_column);
        ELSE RETURN p_column;
    END CASE;
END
```

### 3. View Generation Procedure

```sql
CREATE PROCEDURE generate_masked_view(
    IN p_schema VARCHAR(64),
    IN p_table VARCHAR(64)
)
BEGIN
    DECLARE v_columns TEXT;

    SELECT GROUP_CONCAT(
        CASE
            WHEN pc.mask_type IS NOT NULL
            THEN get_masked_column(p_schema, p_table, c.COLUMN_NAME)
            ELSE c.COLUMN_NAME
        END
    )
    INTO v_columns
    FROM INFORMATION_SCHEMA.COLUMNS c
    LEFT JOIN data_mask_configuration pc
        ON pc.table_schema = c.TABLE_SCHEMA
        AND pc.table_name = c.TABLE_NAME
        AND pc.column_name = c.COLUMN_NAME
    WHERE c.TABLE_SCHEMA = p_schema
    AND c.TABLE_NAME = p_table;

    SET @sql = CONCAT(
        'CREATE OR REPLACE VIEW ', p_schema, '.masked_', p_table,
        ' AS SELECT ', v_columns,
        ' FROM ', p_schema, '.', p_table
    );
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END
```

### 4. Configure Columns

```sql
INSERT INTO data_mask_configuration VALUES
('mydb', 'employees', 'ssn', 'FULL'),
('mydb', 'employees', 'email', 'EMAIL'),
('mydb', 'customers', 'credit_card', 'FULL'),
('mydb', 'customers', 'phone', 'PARTIAL');
```

### 5. Generate Views

```sql
CALL generate_masked_view('mydb', 'employees');
-- Or for all tables:
CALL generate_all_masked_views();
```

### 6. Grant Access

```sql
CREATE USER 'developer'@'%' IDENTIFIED BY 'password';
GRANT SELECT ON mydb.masked_employees TO 'developer'@'%';
-- Deny access to original table
```

## Considerations

**Pros:**
- Real-time masking without data duplication
- Flexible, customizable mask types
- Uses built-in MySQL features
- No additional software required

**Cons:**
- Manual updates required for schema changes
- Performance impact when generating views
- Views don't auto-update when config changes (must regenerate)
- Maintenance overhead

**Performance:**
- High I/O when calling `generate_all_masked_views()`
- CPU utilization increases during view creation
- Consider off-peak regeneration for large tables

## Related

- [[aws-aurora-database-activity-streams]] - Audit logging for Aurora
- AWS RDS Proxy for connection pooling
- AWS Secrets Manager for credential rotation

---
Source: [AWS Database Blog](https://aws.amazon.com/blogs/database/dynamic-view-based-data-masking-in-amazon-rds-and-amazon-aurora-mysql/) (2025-09-19)
