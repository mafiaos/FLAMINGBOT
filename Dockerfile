FROM FLAMING-OS/FLAMINGUSERBOT:slim buster
# clonning repo 
RUN git clone https://github.com/FLAMING-OS/FLAMINGUSERBOT.git /root/userbot


RUN pip install --upgrade pip 
# working directory 
WORKDIR /root/userbot 
# Install requirements


RUN pip3 install -U -r requirements.txt 
ENV PATH="/home/userbot/bin:$PATH" 
CMD ["python3","flamingrun.py"]




