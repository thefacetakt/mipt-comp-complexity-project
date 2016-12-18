cd ..
coverage run -m tests.cnf_utils
mv .coverage coverage/.coverage_cnf_utils
coverage run -m tests.solutions
mv .coverage  coverage/.coverage_solutions
coverage run -m tests.tm
mv .coverage  coverage/.coverage_tm
cd coverage
coverage combine .coverage_*
coverage html
