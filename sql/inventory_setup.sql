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
    supplier_name NVARCHAR(255) NOT NULL,
    contact_name NVARCHAR(255),
    contact_email NVARCHAR(255),
    description NVARCHAR(255), -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);
GO

-- Create the categories table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(255) NOT NULL,
    supplier_id INT NOT NULL,
    description NVARCHAR(255), -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CAS-- filepath: c:\Users\ascop\Documents\Training\Caylent-040125\sql\inventory_setup.sql

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
    supplier_name NVARCHAR(255) NOT NULL,
    contact_name NVARCHAR(255),
    contact_email NVARCHAR(255),
    description NVARCHAR(255), -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);
GO

-- Create the categories table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(255) NOT NULL,
    supplier_id INT NOT NULL,
    description NVARCHAR(255), -- Added description column
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CAS