# Chernobyl001
Data project: Measuring "crows flight-path" between U.S. chemical plants and U.S. K-12 schools.

U.S. Schools Data source: https://nces.ed.gov/ccd/elsi/tableGenerator.aspx
  -Table ID: 120599 //
  
U.S. EPA Chemical Plants Data source: https://echo.epa.gov/tools/data-downloads

Update 1/6/20-
Project went through various iterations, I started by solving the Dataset merge using python with the geopy & google maps API, 
however, the dataset grew too large to compile in memory. From then on I was forced to spin-up a local DB to host all project data
using PostgreSQL and have transitioned project onto Google BQ. This will allow me to maximize the use of BigQuery GIS (https://cloud.google.com/bigquery/docs/gis-intro)
to measure Lat/Lon distances in datasets.
