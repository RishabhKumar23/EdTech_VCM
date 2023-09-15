# import logging package
import logging

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student_id):
        self.students.append(student_id)


class Assignment:
    def __init__(self, details):
        self.details = details


class VirtualClassroomManager:
    # Singleton instance
    _instance = None  

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.classrooms = {}
            cls._instance.assignments = {}
        return cls._instance

    def add_classroom(self, class_name):
        if class_name not in self.classrooms:
            self.classrooms[class_name] = Classroom(class_name)
            print(f'Classroom "{class_name}" has been created. \N{grinning face}')
            logging.info(f'Classroom "{class_name}" has been created. \N{grinning face}')
        else:
            print(f'Classroom "{class_name}" already exists. \N{slightly smiling face}')

    def list_classrooms(self):
        print("List of Classrooms:")
        for class_name in self.classrooms:
            print(class_name)

    def remove_classroom(self, class_name):
        if class_name in self.classrooms:
            del self.classrooms[class_name]
            print(f'Classroom "{class_name}" has been removed. \N{loudly crying face}')
            logging.info(f'Classroom "{class_name}" has been removed. \N{loudly crying face}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist. \N{zipper-mouth face}')

    def enroll_student(self, student_id, class_name):
        if class_name in self.classrooms:
            self.classrooms[class_name].enroll_student(student_id)
            print(f'Student "{student_id}" has been enrolled in "{class_name}" class. \N{grinning face}')
            logging.info(f'Student "{student_id}" has been enrolled in "{class_name}" class. \N{grinning face}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist. \N{zipper-mouth face}')

    def list_students(self, class_name):
        if class_name in self.classrooms:
            print(f'Students in "{class_name}": {", ".join(self.classrooms[class_name].students)} \N{grinning face}')
            logging.info(f'Students in "{class_name}": {", ".join(self.classrooms[class_name].students)} \N{grinning face}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist. \N{grinning face}')

    def schedule_assignment(self, class_name, assignment_details):
        if class_name in self.classrooms:
            self.assignments[class_name] = Assignment(assignment_details)
            print(f'Assignment for "{class_name}" has been scheduled. \N{grinning face}')
            logging.info(f'Assignment for "{class_name}" has been scheduled. \N{grinning face}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist. \N{zipper-mouth face}')

    def submit_assignment(self, student_id, class_name, assignment_details):
        if class_name in self.classrooms:
            if student_id in self.classrooms[class_name].students:
                print(f'Assignment submitted by Student "{student_id}" in "{class_name}" class. \N{grinning face}')
                logging.info(f'Assignment submitted by Student "{student_id}" in "{class_name}" class. \N{grinning face}')
            else:
                print(f'Error: Student "{student_id}" is not enrolled in "{class_name}" class. \N{zipper-mouth face}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist. \N{zipper-mouth face}')

    def design_pattern(self):
        print( 
            '''
                                                             About Design Pattern\N{grinning face}
            ===============================================================================================================================
            | The design pattern used in this application is **Composite Pattern** and **Singleton Pattern**.                             |
            |                                                                                                                             |    
            | ### Composite Pattern:                                                                                                      |        
            | The Composite Pattern is a structural design pattern that allows you                                                        |        
            | to compose objects into tree structures to represent part-whole hierarchies.                                                |            
            | In this pattern, individual objects and compositions of objects are treated uniformly.                                      |        
            |                                                                                                                             |    
            | In our case:                                                                                                                |
            | - **Classroom** and **Assignment** are the leaf nodes of the composite tree.                                                |
            | - **VirtualClassroomManager** acts as the composite, managing the composition of classrooms and assignments.                |    
            |                                                                                                                             |    
            | By using the Composite Pattern, the VirtualClassroomManager can treat both individual                                       |
            | classrooms and assignments (leaf nodes) and composite structures (classrooms containing assignments)                        |    
            | uniformly through a common interface.                                                                                       |        
            |                                                                                                                             |
            | Additionally, the **Singleton Pattern** is indirectly used for managing the VirtualClassroomManager instance,               | 
            | ensuring that there is a single point of access to the functionality of managing classrooms, students, and assignments.     |
            |                                                                                                                             |    
            | ### Singleton Pattern:                                                                                                      |    
            | The Singleton Pattern is a creational design pattern that ensures a class has only one instance                             |
            | and provides a global point of access to that instance.                                                                     |
            |                                                                                                                             |
            | In this case:                                                                                                               |                                                               
            | - The VirtualClassroomManager is instantiated only once at the beginning of the program,                                    |
            | and subsequent requests reuse this instance throughout the program.                                                         |
            |                                                                                                                             |    
            | These patterns help in achieving better organization, reusability, and maintainability of the codebase.                     |
            | The Composite Pattern facilitates the management of the composite structure of classrooms and assignments,                  |
            | while the Singleton Pattern ensures that there is a single, globally accessible point for managing these entities.          |
            |                                                                                                                             |
            ===============================================================================================================================

            '''
        )
        return True

# To take record of all the actions 
def setup_logging():
    logging.basicConfig(filename='application.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


# Initialize the Virtual Classroom Manager
manager = VirtualClassroomManager()
setup_logging()

while True:
    print(
            '''
                                            Welcome TO EdTECH
            ===============================================================================
            | Select an action (1, 2, 3, 4, 5, 6, 7, 8):                                  |
            |  1. Add Classroom                                                           |      
            |  2. List Classrooms                                                         |  
            |  3. Remove Classroom                                                        |  
            |  4. Enroll Student                                                          |  
            |  5. List Students                                                           |  
            |  6. Schedule Assignment                                                     |  
            |  7. Submit Assignment                                                       |      
            |  8. To Know Which Design pattern i use and why (pls use full screen)        |  
            |  0. Exit                                                                    |   
            ===============================================================================
            '''
        )
    user_choice = input("Choose Option: ")

    if user_choice == '1':
        class_name = input("Enter the classroom name: ")
        manager.add_classroom(class_name)

    elif user_choice == '2':
        manager.list_classrooms()

    elif user_choice == '3':
        class_name = input("Enter the classroom name to remove: ")
        manager.remove_classroom(class_name)

    elif user_choice == '4':
        student_id = input("Enter the student ID: ")
        class_name = input("Enter the classroom name to enroll the student: ")
        manager.enroll_student(student_id, class_name)

    elif user_choice == '5':
        class_name = input("Enter the classroom name to list students: ")
        manager.list_students(class_name)

    elif user_choice == '6':
        class_name = input("Enter the classroom name: ")
        assignment_details = input("Enter the assignment details: ")
        manager.schedule_assignment(class_name, assignment_details)

    elif user_choice == '7':
        student_id = input("Enter the student ID: ")
        class_name = input("Enter the classroom name: ")
        assignment_details = input("Enter the assignment details: ")
        manager.submit_assignment(student_id, class_name, assignment_details)
    
    elif user_choice == '8':
        if not manager.design_pattern():
            break

    elif user_choice == '0':
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
