# Python CRUD Application for Hospital

A comprehensive Python application for managing inpatient (patient who stays in a hospital while under treatment) data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the health industry, specifically addressing the need to manage inpatient data efficiently. Managing inpatient data is crucial to monitor the condition of inpatients to determine treatment prioritization.

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data
* Allows to easily monitor inpatient status

**Target Users:**

This application is designed for inpatient administrators, doctors, and nurses within the organization to facilitate their data collecting and treatment related to inpatient.

## Features

* **Create:**
    * Add new inpatient entries with essential details like room number, admission date, and patient status.
    * Implement validation rules to ensure data integrity
    * Automatically generate unique ID when inserting new data
* **Read:**
    * Search and retrieve specific inpatient records by applying filters based on patient ID.
    * Display comprehensive information for each inpatient in a user-friendly format.
* **Update:**
    * Modify existing inpatient data to reflect changes in patient status.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted inpatient records with appropriate authorization checks (if applicable).
    * Implement soft delete functionality to prevent permanent data loss.


## Installation

1. **Prerequisites:**
    * Python version 3.8 or higher

2. **Installation:**
    ```bash
    git clone https://github.com/KevianwillieHandoyo/capstone_python_crud.git
    cd capstone_python_crud
    ```


## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new inpatient record.
    * **Read:** Show all existing data, and search a specific patient by their patient ID.
    * **Update:** Modify customer details, such as updating their address or contact details.
    * **Delete:** Remove a customer record from the system (with appropriate authorization, if applicable).

## Data Model
This project utilizes a list to represent inpatient data. The following fields are stored:
   * ID: String - Description of the field's purpose in the business context.
   * Nama: String - Description of the field's purpose in the business context.
   * Umur: Int - Description of the field's purpose in the business context.
   * Tanggal Masuk RS: String - Description of the field's purpose in the business context.
   * Nomor Kamar: Int - Description of the field's purpose in the business context.
   * Status: String - Description of the field's purpose in the business context.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to kevianwillie.h@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

