"""Re-runs the measured pipeline end to end (needs the raw files in data/raw/)."""
import subprocess, sys
for s in ['src/ingest_houselisting.py','src/real_ownership_model.py','src/real_clusters.py','src/real_score.py']:
    print('==',s); r=subprocess.run([sys.executable,'-I',s]); 
    if r.returncode: sys.exit(r.returncode)
