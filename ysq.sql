-- delimiter $$
-- create procedure p_test()
-- begin
-- declare num int;
-- set num = 10;
-- select num;
-- end $$
-- delimiter ;


-- delimiter $$
-- create function score_q(id1 int,id2 int)
-- returns float
-- begin
-- set @s1 =(select score from 一班 where id = id1 );
-- set @s2 =(select score from 一班 where id = id2 );
-- return (@s1-@s2);
-- end $$



set session transaction isolation level read committed  