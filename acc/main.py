from saramin import get_jobs as get_saramin_jobs
from save import save_to_file

saramin_jobs = get_saramin_jobs()
jobs = saramin_jobs
save_to_file(jobs)
