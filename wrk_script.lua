wrk.timeout = 2000

function error(err)
    print("ERROR: " .. err)
end

function response(status, headers, body)
    if status ~= 200 then
        print("ERROR " .. status )
    end
end
--  wrk -t10 -c900 -d5s -s wrk_script.lua http://localhost:8001/gunicorn/
--  wrk -t10 -c1100 -d5s -s wrk_script.lua http://localhost:8001/gunicorn/
-- по идее на 1000 тоже обычно нет ошибок, но иногда бывают, так что 9000 (настоящий rps 10000, т.к. 10 потоков)

