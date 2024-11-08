install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

train:
	python train.py

eval:
	echo "## Model Metrics" > report.md
	cat ./Output/metrics.txt >> report.md
	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](./Output/model_results.png)' >> report.md
	cml comment create report.md

hf-login:
	git pull origin update
	git switch update
	pip install -U "huggingface_hub[cli]"
	huggingface-cli login --token $(HF) --add-to-git-credential

push-hub:
	huggingface-cli upload CTCD_for_Machine_Learning_Models ./App --repo-type=space --commit-message="Sync App files"
	huggingface-cli upload CTCD_for_Machine_Learning_Models ./Model /Model --repo-type=space --commit-message="Sync Model"
	huggingface-cli upload CTCD_for_Machine_Learning_Models ./Output /Metrics --repo-type=space --commit-message="Sync Model"

deploy:
	hf-login push-hub
