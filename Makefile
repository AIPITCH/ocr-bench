all: run

run:
	@./run.py

dry-run:
	@./run.py -d

clean-samples:
	@rm -f samples/*.pdf-*
	@rm -f samples/*_bboxes.png

clean-run-results:
	@rm -f run_results/*

.PHONY: run dry-run clean-samples clean-run-results
