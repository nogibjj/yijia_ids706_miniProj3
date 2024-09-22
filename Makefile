install: 
	pip3 install --upgrade pip && pip3 install -r requirements.txt

format: 
	black *.py

lint:
	flake8 --ignore=E501 *.py

test: 
	python3 -m pytest -cov=main test_main.py

clean:
	rm -rf .pytest_cache

generate_report:
	python -c "from main import load_data, calculate_statistics, create_histogram, generate_md_report; \
	data = load_data('rdu-weather-history.csv'); \
	stats = calculate_statistics(data); \
	create_histogram(data, 'Temperature Maximum', 'temperature_maximum_distribution.png'); \
	generate_md_report(stats, ['temperature_maximum_distribution.png'], 'summary_report.md')"
	
   # Git commands to add, commit, and push the report and PNG files
	@if [ -n "$$(git status --porcelain)" ]; then \
	    git config --local user.email "action@github.com"; \
	    git config --local user.name "GitHub Action"; \
	    git add summary_report.md temperature_maximum_distribution.png; \
	    git commit -m 'Add generated markdown report and histogram image'; \
	    git push; \
	else \
	    echo "No changes to commit."; \
	fi

all: install format lint test generate_report