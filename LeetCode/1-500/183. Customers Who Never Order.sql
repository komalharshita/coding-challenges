select Name as Customers
from Customers
where Id not in (
    select CustomerId 
    from Orders)


-- optimized version 

select c.Name as Customers
from Customers c
left join Orders o on c.Id = o.CustomerId  -- Join on indexed foreign key
where o.CustomerId is null                 -- Keep only customers with no matching orders