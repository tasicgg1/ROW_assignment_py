# ROW_assignment_py
This script can be used for ROW results to assign splice names to the buildings 

In order to use this script, you must have installed Python, and you must change some parts of the code to match the code to your PC. 
Please follow each step carefully:

1. You must have installed Python on your local machine,
2. You must have created an environment and installed geopandas and pandas libraries in your environment on your local machine,
3. You need to pull all files from my GitHub and save them in your custom folder. All files must be in the same folder,
4. In your folder on your local machine do the following steps,
5. In the file "run_process.bat" you must change the path to your environment folder (change this part: C:\Users\TASA\anaconda3\envs\geo_env\),
6. You need to replace files: "buildings.csv", "ROW_path.gpkg", and "splice_points.gpkg" with your files but the names of the files MUST stay the same,
7. If you have from Alter Engine more than one file from above mentioned, combine them in one and save it with appropriate extensions (.csv or .gpkg),
8. File "buildings.csv" must be in TCW format and must have column "ROW Distance 1 Access Point". In this column will be the result at the end in a new file,
9. File "splice_points" must have column "name", this column needs to be populated with information that you want to assign to the buildings, this column is MUST,
10. Once you updated all three files, and changed the .bat file. To run the script you need to double-click on the file "run_process.bat" this will start up calculating,
11. After double click on the "run_process.bat" cmd prompt will appear, do not close it. It will close automatically after the process is done,
12. After the process is done, in the same folder will appear the file "buildings_new.csv" This is your final file and in the column "ROW Distance 1 Access Point" are assigned names of splice points to whom belongs buildings,
13. Now you can use this file to finish your task.
14. If you have some problems or if the script gives bad results, please contact me.

Thanks.

