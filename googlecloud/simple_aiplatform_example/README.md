# Simple AI Platform example for demonstration purposes

Run the following, changing the '--staging-bucket'.

gcloud ai-platform jobs submit training 'renato1' \
--staging-bucket gs://renatoleite-nb/ \
--package-path trainer \
--module-name trainer.task \
--region us-east1 \
--runtime-version 2.1 \
--python-version 3.7 \
-- \
--learning-rate=0.1