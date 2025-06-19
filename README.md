### Project Title
-----------------------------
## End To End Resume ATS Tracking LLM Project With Google Gemini Pro
--------------------------------
#### Descriptions
----------------


### Use tools and Libraries
 - Code Editor --> Visual Studio Code Editor
 - Language --> python
 - frontend --> streamlit(python web Framework)
 - Host --> github
 - LLm API  --> Google gemini pro 
--------------
# STEPS to create Project
1. Environment setup
    - `conda create -p atsenv python==3.10 -y`
    - Activate environemt `conda activate atsenv/`
2. Create the requirements.txt to install important libraries and framework
    - IN requirements.txt add important libraries and framework
    - Save and run CMD `pip install -r requeriment.txt` 

3. create .env file in project folder to save the api key secure
    - Go to browser and search "Makersuite"
    - signup and click on create API key  
    - copy the api key and paste in .env file
    - `GOOGLE_API_KEY = 'YOUR_API_KEY'`
4. Deacribe the workFlow of website
    - setup poppler 
    - api integrate
    - pdf to text --> pypdf
    - text pass to API and return response
    - 
4. Create the app.py to develop application code
    - Import all requirements
    - Create get_gemini_response function to get the model and pass the input
    - Create the input_pdf_text fuction to extract text from pdf
    - Create a prompt_input variable  where pass the prompt template of response
    - Create a Basic streamlit app functionality in app

5. RUN THE APP 
    - Open to CMD 
    - Go to the project folder where the app.py 
    - run `streamlit run app.py`
    - then go to browser paste `Local URL: http://localhost:8501`





