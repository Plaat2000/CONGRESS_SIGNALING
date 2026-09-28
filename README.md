  docker-compose.yml
  requirements.txt
  db/
    schema.sql
    models.py
  ingestion/
    committees.py
    trades.py
    prices.py
    lobbying.py
    legislation.py
  analysis/
    signals_sql.sql
    signals_notebook.ipynb  # optional# congress_signals

# CONGRESS_SIGNALING

## Webinterface

Start the read-only webinterface from the repository root:

```bash
python webinterface.py
```

Open http://127.0.0.1:8000/ in a browser. Use the `senator` and `ticker`
fields to filter signals. Machine-readable results are available at
`/api/trades`; `/health` can be used as a basic availability check.
