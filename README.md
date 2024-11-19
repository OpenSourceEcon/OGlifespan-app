# OGlifespan-app
This repository contains the files and data necessary to execute single parameterization interpolation of the OG-USA model output.

## Steps
1. Download or clone this repository and its files and file structure to your local machine.
2. Navigate in your browser to the folder of the [https://github.com/rickecon/OGlifespan-app](https://github.com/rickecon/OGlifespan-app)
3. Create the `oglife-app-dev` conda environment using the `environment.yml` file in the repository: `conda env create -f environment.yml`.
4. Activate the `oglife-app-dev` conda environment: `conda activate oglife-app-dev`
5. Run the following code, which will generate the web app in a local server: `python main.py`
6. Paste the URL address of the server listed in your terminal output into your terminal URL bar.
7. This is the web application.

## Files in the repository
- `.gitignore`: Tells `git` which files to not track with GitHub.
- `app.yml`: We don't use this for the local test use case above, but this file is valuable for posting an app like this on Google's App Engine.
- `environment.yml`: Gives a list of the Python packages necessary for running the instructions in this code base.
-`interp_rbf_OGlifesense.pkl`: Python pickled binary version of `Scipy.interpolator` estimated on the model data.
- `LICENSE`: Open source license for the project.
- `main.py`: This is the main Python file that defines and executes the page.
- `README.md`: Instructions for this repository.
- `requirements.txt`: We don't use this for the local test use case above, but this file is valuable for posting an app like this on Google's App Engine.
- `static/mystyle.css`: CSS style file for the web application.
- `templates/index.html`: HTML file that calls the flask app.
