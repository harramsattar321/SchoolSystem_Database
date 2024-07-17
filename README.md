


# School System DBMS

## Description
The  School Database offers a comprehensive collection of crucial educational data sourced from the census. In this database system, the detailed data of schools in Pakistan, including building data, location, staff data, subjects, and other related information, is provided. Accessible to policymakers, researchers, educators, and stakeholders, it serves as a foundational resource for analyzing educational landscapes, identifying trends, and formulating evidence-based policies and interventions to enhance educational quality and accessibility in the region during the census year of 2018.

### Purpose
- To centralize information about all public schools in Pakistan.
- To provide detailed profiles for each school, including demographic information, infrastructure details, staff, etc.
- To enable educational policymakers, researchers, and stakeholders to conduct in-depth analysis of the educational landscape.
- To facilitate ongoing monitoring and evaluation of schools across different regions, enabling the identification of areas needing improvement and the assessment of the effectiveness of educational initiatives.
- To assist in the equitable allocation of resources by providing insights into the distribution of schools, student demographics, and educational needs across various regions and demographics within Pakistan.
- To promote transparency and accountability in the education sector by making school-related data readily accessible to the public.

### Functionality
- Maintain detailed profiles for each school.
- Catalog information about school facilities including classrooms, laboratories, libraries, playgrounds, and other amenities.
- Manage data related to teaching staff.
- Analyze data to inform resource allocation decisions, ensuring equitable distribution of educational resources based on identified needs and priorities.
- Provide a public-facing portal to disseminate aggregated educational data, school profiles, and performance indicators to enhance transparency and accountability in the education sector.
- Monitor compliance with educational regulations, standards, and policies, ensuring adherence to quality assurance guidelines.

## System Requirements
### Software
- Operating System: Windows
- Database Management System: MySQL
- Programming Language: Python 3.x
- Libraries/Frameworks: Tkinter

### Hardware
- No specific hardware requirements

## Installation Instructions
1. **Install Python**
   - Download and install Python 3.x from [here](https://www.python.org/downloads/).

2. **Install Required Libraries**
   ```sh
   pip install mysql-connector-python
   pip install tk  # Tkinter
   ```

3. **Set Up the Database**
   - Get the `.sql` file from the attached folder.
   - Open MySQL and create the database:
    
   - Import the `.sql` file:
     ```sh
     mysql source  path/to/filename.sql
     ```

4. **Run the Frontend**
   ```sh
   python frontend.py
   ```

## Usage Instructions
1. **Access the Application**
   - Open the application by running `frontend.py`.

2. **Navigate through the System**
   - The main window will display five buttons: **Insert**, **Delete**, **Modify**, **Search**, and **Display**.

3. **Perform Administrative Tasks**
   - **Insert**: Click the **Insert** button to open a menu bar with the names of all tables (Building, Building_Lab, Contact_Info, Game, Game_School, Head, Lab, School, Union_Council). Select the desired table to insert new records.
   - **Delete**: Click the **Delete** button to open a menu bar with the names of all tables. Select the desired table to delete existing records.
   - **Modify**: Click the **Modify** button to open a menu bar with the names of all tables. Select the desired table to modify existing records.
   - **Search**: Click the **Search** button to open a menu bar with the names of all tables. Select the desired table to search for specific records.
   - **Display**: Click the **Display** button to open a menu bar with the names of all tables. Select the desired table to display all records in that table.

## Code Structure Overview
```
school-system-dbms/
│
├── frontend.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── insertbuilding.py
│   ├── insertschool.py
│   ├── insertbuildinglab.py
│   ├── insertcontact_info.py
│   ├── insertgame.py
│   ├── insertgameschool.py
│   ├── inserthead.py
│   ├── insertlab.py
│   ├── insertuc.py
│   ├── deleteschool.py
│   ├── deletebuilding.py
│   ├── deletecontactinfo.py
│   ├── deletegame.py
│   ├── deletehead.py
│   ├── deletelab.py
│   ├── deleteuc.py
│   ├── deletebuildinglab.py
│   ├── deleteschoolgame.py
│   ├── searchschool.py
│   ├── searchuc.py
│   ├── searchlab.py
│   ├── searchhead.py
│   ├── searchgame.py
│   ├── searchcontactinfo.py
│   ├── searchbuilding.py
│   ├── searchgameschool.py
│   ├── searchbuildinglab.py
│   ├── displayschool.py
│   ├── displaybuilding.py
│   ├── displaybuildinglab.py
│   ├── displaycontactinfo.py
│   ├── displaygame.py
│   ├── displaygameschool.py
│   ├── displayhead.py
│   ├── displaylab.py
│   ├── displayuc.py
│   ├── modifyschool.py
│   ├── modifybuilding.py
│   ├── modifycontactinfo.py
│   ├── modifygame.py
│   ├── modifyhead.py
│   ├── modifylab.py
│   ├── modifyuc.py
│
└── helpers/
    ├── db_connection.py
```

- **`frontend.py`**: Main file to run the application.
- **`modules/`**: Contains files for inserting, deleting, modifying, searching, and displaying data.




