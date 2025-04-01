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

-- Create the `suppliers` table
CREATE TABLE suppliers (
    supplier_id INT IDENTITY(1,1) PRIMARY KEY,
    supplier_name NVARCHAR(255) NOT NULL,
    contact_name NVARCHAR(255),
    contact_email NVARCHAR(255),
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    Description VARCHAR(255) NULL -- Added Description column
);
GO

-- Create the `categories` table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(255) NOT NULL,
    supplier_id INT NOT NULL,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    Description VARCHAR(255) NULL, -- Added Description column
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
GO

-- Create the `products` table
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name NVARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    -- add a boolean collumn 'active' to indicate if the product is active or not
    active BIT NOT NULL DEFAULT 1,
    -- add a column 'image_url' to store the URL of the product image
    image_url NVARCHAR(255) NULL,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    Description VARCHAR(255) NULL, -- Added Description column
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
GO