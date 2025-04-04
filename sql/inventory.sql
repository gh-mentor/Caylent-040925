-- Step 1: Database Setup
IF DB_ID('Inventory') IS NOT NULL
BEGIN
    DROP DATABASE Inventory;
END;
GO

CREATE DATABASE Inventory;
GO

USE Inventory;
GO

-- Step 2: Table Creation

-- Create the suppliers table
CREATE TABLE suppliers (
    supplier_id INT IDENTITY(1,1) PRIMARY KEY,
    supplier_name NVARCHAR(100) NOT NULL,
    contact_name NVARCHAR(100),
    phone NVARCHAR(20),
    description VARCHAR(255) NULL, -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);
GO

-- Create the categories table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(100) NOT NULL,
    supplier_id INT NOT NULL,
    description VARCHAR(255) NULL, -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);
GO

-- Create the products table
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name NVARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    description VARCHAR(255) NULL, -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);
GO

-- Step 3: Data Population

-- Populate the suppliers table
INSERT INTO suppliers (supplier_name, contact_name, phone, description)
VALUES 
('Supplier A', 'John Doe', '123-456-7890', 'Electronics supplier'),
('Supplier B', 'Jane Smith', '987-654-3210', 'Furniture supplier'),
('Supplier C', 'Alice Johnson', '555-555-5555', 'Clothing supplier');
GO

-- Populate the categories table
INSERT INTO categories (category_name, supplier_id, description)
VALUES 
('Electronics', 1, 'Electronic devices and gadgets'),
('Furniture', 2, 'Office and home furniture'),
('Clothing', 3, 'Apparel and accessories');
GO

-- Populate the products table
INSERT INTO products (product_name, category_id, price, stock, description)
VALUES 
('Laptop', 1, 999.99, 50, 'High-performance laptop'),
('Desk', 2, 199.99, 20, 'Wooden office desk'),
('T-Shirt', 3, 19.99, 100, 'Cotton t-shirt'),
('Smartphone', 1, 699.99, 30, 'Latest model smartphone'),
('Chair', 2, 89.99, 40, 'Ergonomic office chair'),
('Jeans', 3, 49.99, 60, 'Denim jeans');
GO

-- Step 4: Additional Features

-- Create a view to display product, category, and supplier details
CREATE VIEW product_list AS
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    p.stock,
    p.description AS product_description,
    c.category_name,
    s.supplier_name,
    s.phone AS supplier_phone
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
JOIN 
    suppliers s ON c.supplier_id = s.supplier_id;
GO

-- Create a stored procedure to retrieve the product_list view
CREATE PROCEDURE GetProductList
AS
BEGIN
    SELECT * FROM product_list;
END;
GO

-- Add a trigger to update the products table when a categories record is deleted
CREATE TRIGGER trg_UpdateProductsOnCategoryDelete
ON categories
AFTER DELETE
AS
BEGIN
    UPDATE p
    SET p.category_id = NULL
    FROM products p
    JOIN deleted d ON p.category_id = d.category_id;
END;
GO

-- Create a function to calculate the total number of products in a category
CREATE FUNCTION TotalProductsInCategory (@CategoryId INT)
RETURNS INT
AS
BEGIN
    RETURN (SELECT COUNT(*) FROM products WHERE category_id = @CategoryId);
END;
GO

-- Create a function to calculate the total number of products supplied by a supplier
CREATE FUNCTION TotalProductsBySupplier (@SupplierId INT)
RETURNS INT
AS
BEGIN
    RETURN (
        SELECT COUNT(*)
        FROM products p
        JOIN categories c ON p.category_id = c.category_id
        WHERE c.supplier_id = @SupplierId
    );
END;
GO