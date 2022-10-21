# Computer Vision Rock Paper Scissors

## macOS Setup
This section will walk you through how to properly setup all the dependencies for this particular project. Please note that I am working on an Apple Silicon (M1) MacBook Pro, so your mileage may vary if you are working on an Intel-based Mac. Please be sure to follow these steps closely as this can be a challenging project to set up. If you have not already done so, you will need to ensure you already have Homebrew and Python installed on your machine. For context, the precise version of Python that I ran on my Mac when completing this project was Python 3.10.7.

https://github.com/tensorflow/io/issues/1625#issuecomment-1128555922

1. Establish a new Python virtual environment in your Git repository by running the following command: `python3 -m venv venv`.
2. Activate the Python virutal enviornment by running the following command: `source venv/bin/activate`
3. Install the Python dependencies noted in the `dependencies/requirements.txt` file by running the following: `pip3 install -r dependencies/requirements.txt`.

## Troubleshooting
This section will include tips for troubleshooting.

### Image Annotation with Label Studio
**Q: I'm on an Apple Silicon (M1) Mac and am having trouble getting Label Studio to installing it via the `pip` install. The error notes something wrong with the `psycopg2-binary`. What do I do?**

A: You will need to pre-install Postgres to your machine before re-running the Label Studio `pip` install. The following steps will resolve your issue. (And special thanks to [this person](https://www.bruno-giarrizzo.fr/tricks/2021/10/17/how-to-install-psycopg2-binary-on-apple-m1.html) for figuring out the solution to this problem!)

1. Use homebrew to install Postgres with this command: `brew install postgresql@12`
2. Update your local `.zshrc` file with this line: `export PATH="/opt/homebrew/opt/postgresql@12/bin:$PATH"`. If you're not a stickler for organization in your `.zshrc` file, you may also simply add this line to your `.zshrc` file by running this command: `echo 'export PATH="/opt/homebrew/opt/postgresql@12/bin:$PATH"' > ~/.zshrc`
3. Restart your Terminal / iTerm2 in order for the changes in the previous step to take.
4. Install `psycopg2` with the following command: `pip3 install psycopg2-binary`.
5. Re-run `pip3 install label-studio` to successfully install Label Studio!

**Q: I've successfully installed Label Studio via the `pip` install on my Apple Silicon (M1) Mac but am having trouble getting it started. This is the error message I'm seeing: `AttributeError: module 'rest_framework.serializers' has no attribute 'NullBooleanField'. Did you mean: 'BooleanField'?` What do I do?**

A: As of September 2022, it appears that the Python library `djangorestframework` updated some field in newer versions and Label Studio hasn't been updated properly to account for this. To remedy, you will need to downgrade your version of this particular library by running the following command: `pip3 install djangorestframework==3.13.1`.

**Q: I am on an Apple Silicon (M1) Mac running Python 3.10, and after installing Label Studio via `pip`, I am having difficulty getting it started due to the following error: `ImportError: dlopen(/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/google/protobuf/pyext/_message.cpython-310-darwin.so, 0x0002): symbol not found in flat namespace (__ZN6google8protobuf15FieldDescriptor12TypeOnceInitEPKS1_)`. What do I do?**

A: From what I discovered via [this GitHub issue](https://github.com/protocolbuffers/protobuf/issues/10571), it appears this is a current known issue with a newer version of the `protobuf` Python library. Downgrading the version fixes the issue by running the following command: `pip3 install protobuf==3.20.1`.