# Real-World IoT Monitoring Scenario

Development of a system to monitor the number of people entering/leaving a classroom/lab by resorting to Object-Oriented Programming with Python and Advanced software testing using unittest.

An initial set of public tests was provided for initial software development, with new public tests made available periodically for software code refactoring.

The developed system was simulated in WOKWI and is available [here](https://wokwi.com/projects/334412072311849556).

The figure below depicts its conceptualisation (on the left) and implementation (on the right):
![DTSD IoT Monitoring System](https://github.com/ro-afonso/dIoTspmatrix_55007_56336/assets/93609933/2ff0d86b-6810-4a80-8e85-b18bdb51e21a)


The system includes the following functionalities:
* Log the number of people using a motion sensor (PIR motion sensor)
* Record logs each minute in a matrix with 24 lines [0:23] representing hours and 60 columns [0:59] representing minutes.
* Each matrix element encloses the number of occurrences detected by the motion sensor.
* Representation of the matrix is sparse as enter and leave the meeting room only from time to time and also the meeting room is not used during off-office hours
* Communicate via MQTT using JSON messages with payload using a normalised data representation for sparse matrices (compressed format)
* Store & Load data locally (in node) to prevent data loss (due to any reason)
* Display data (locally, at the edge) in a visualisation dashboard (OLED) using a pixelized heatmap representation for the logs
