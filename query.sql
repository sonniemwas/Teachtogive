SELECT 
    d.driver_name,
    d.driver_nationality,
    r.race_name,
    r.circuit_location,
    res.position,
    res.grid,
    res.fastest_lap,
    res.points,
    t.team_name,
    r.race_date
FROM 
    races r
JOIN 
    results res ON r.race_id = res.race_id
JOIN 
    drivers d ON res.driver_id = d.driver_id
JOIN 
    constructors t ON res.constructor_id = t.constructor_id
WHERE 
    r.race_year = 2020
ORDER BY 
    res.points DESC;
