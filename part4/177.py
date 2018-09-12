# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
# declare X int;
# set X = N-1;
#   RETURN (
#       # Write your MySQL query statement below.
#           select distinct salary
#           from employee
#           order by salary DESC
#           limit 1 offset X
#   );
# END