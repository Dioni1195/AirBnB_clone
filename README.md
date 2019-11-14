# 0x00. AirBnB clone - The console
---
<img align="center" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png"  width="100%"/>

## Holberton School Airbnb Clone - Command Interpreter Project Description
---
This is the first of a multipart project working towards building a full web application clone of AirBnb.
In this first part, the Python programming language is used to build a command interpreter
for the clone's web app. This command interpreter is similar to a BASH shell but it is designed
for a specific use case. The following projects will incorporate additional sections like HTML/CSS 
templating, database storage, API and front-end integration.

### Start the interpreter
---
In the command line run `./console.py` or `echo help | ./console.py`

### Usage
---

This interpreter has basic console commands

Command | Syntax | Output
------- | ------ | ------
help | `help *[option]*` | Lists all available commands, or displays what option does
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id


### Files
---
File Name | Description
--- | ---
`models/base_model.py` | Base Class with public instance attributes and methods
`models/amenity.py` | An amenity class that inherits from BaseModel
`models/city.py` | A city class that inherits from BaseModel
`models/place.py` | A place class that inherits from BaseModel
`models/review.py` | A review class that inherits from BaseModel
`models/state.py` | A state class that inherits from BaseModel
`models/user.py` | A user class that inherits from BaseModel
`models/engine/file_storage.py` | A class that serializes instances to a JSON file and deserializes JSON file to instances
`tests/test_models/` | Unittests for BaseModel, User, amenity, city, place, review, and state
`tests/test_models/test_engine/` | Unittest for file storage


## Example Usage
---
```python3
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb) create User
bfb1f012-ae50-493a-816b-c0e246194084
(hbnb) User bfb1f012-ae50-493a-816b-c0e246194084
*** Unknown syntax: User bfb1f012-ae50-493a-816b-c0e246194084
(hbnb) show User bfb1f012-ae50-493a-816b-c0e246194084
[User] (bfb1f012-ae50-493a-816b-c0e246194084) {'created_at': datetime.datetime(2019, 11, 13, 8, 59, 26, 921714), 'updated_at': datetime.datetime(2019, 11, 13, 8, 59, 26, 921798), 'id': 'bfb1f012-ae50-493a-816b-c0e246194084'}
(hbnb) update User bfb1f012-ae50-493a-816b-c0e246194084 name Dionisio
(hbnb) show User bfb1f012-ae50-493a-816b-c0e246194084
[User] (bfb1f012-ae50-493a-816b-c0e246194084) {'id': 'bfb1f012-ae50-493a-816b-c0e246194084', 'updated_at': datetime.datetime(2019, 11, 13, 9, 1, 11, 81029), 'name': 'Dionisio', 'created_at': datetime.datetime(2019, 11, 13, 8, 59, 26, 921714)}
```
## Data diagram
---

This diagram represents how the classes are connected each other and their main attributes

![PlantUML model](http://www.plantuml.com/plantuml/png/ZPBDRjim3CVlUWeTjqFUO8Ti0NRQiA4v5eL0oup3LX-6IES3RTwzifGuYNFfIN_-I1Ca_rwoG9B1EwKKlr7e8O7NFePejobwr986LCewODQ_WF5lRD7fTsKC1H9ZldtFaYKLnR33_4WqBLd9QdoqsP13quDirHzYUNxH9ZQlQ8NLwTpvfyVSxPZx1l0uuLLbB21egBrF_dTWCMUrrZRNZVai1yPqbgKwlosoJTGBnL3mu9jSasBqV1CtURw9UJYORa2MCUWJMJJDqGJgjeKu49AXnQ9ZwAO0F8OwotMt9zmHxkkW_JZpuwI21pdLwlMuw-mCOsNv73sGAtqotiTKFjvGOZ6NPHrSWjF5jj_aS2qnGPSRWtFPbu3xgrq9NOJsIswfVqNg7n-BnMtVEpxz9cfIDN5sUOvNZwoQEuVraZDQBpQ3vMHABJ6qWtUV)

Authors:
* **Dionisio Arango** - *Initial Work and Documentación* - [Dioni1195](https://github.com/Dioni1195)
* **Juan F. Calle** - *Initial Work and Documentación* - [johnconnor77](https://github.com/johnconnor77)

