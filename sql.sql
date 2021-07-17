SELECT
  LOWER(o.object_name) AS proc_name,
  LOWER(o.object_type) AS proc_kind,
  LOWER(CASE
    WHEN a.data_type IS NULL THEN 'void'
    WHEN a.data_type = 'CHAR' THEN 'CHAR(' || a.data_length || ')'
    WHEN a.data_type = 'VARCHAR2' THEN 'VARCHAR2(' || a.data_length || ')'
    WHEN a.data_type = 'NUMBER' THEN 'NUMBER(' || NVL(a.data_precision, 0) || ',' || NVL(a.data_scale, 0) || ')'
    ELSE a.data_type END) AS return_type,
  LOWER(CASE
    WHEN a.argument_name IS NULL THEN '-'
    ELSE a.argument_name END) AS return_name,
  s.src as src
FROM all_objects o
  LEFT JOIN sys.all_arguments a ON a.object_id = o.object_id
    AND a.in_out = 'OUT'
  JOIN (
    SELECT
      s.name as name,
      listagg(s.text) WITHIN GROUP (ORDER BY s.line) AS src,
      s.owner as owner
    FROM all_source s
    GROUP BY s.name
  ) AS s ON s.owner = o.owner
  AND s.name = o.object_name
WHERE o.object_type IN ('FUNCTION','PROCEDURE')
  AND o.owner = UPPER('db_name')
ORDER BY o.object_id;
