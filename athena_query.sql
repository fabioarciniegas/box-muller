with last_hour_events as (
SELECT 1440+(cast(floor((to_unixtime(current_timestamp-interval '24' hour))/60) as int)-one_minute_window) as minutes_ago, SUM(event_count) as total_events FROM (
SELECT
  floor((timestamp/1000)/60) AS one_minute_window,
  COUNT(*) AS event_count
FROM waf_logs
where timestamp/1000 >= to_unixtime(current_timestamp-interval '24' hour)
GROUP BY 1 order by 1)
GROUP BY 1
order by 1)

SELECT cast(numeric_histogram(30,total_events,1) as json) from last_hour_events as json;