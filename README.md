# Maruti Suzuki, Mumbai showroom site selection

## Status (honest)
| Part | State |
|---|---|
| Charter, hypotheses, source register | Done (`stage_01_02_project_charter_and_source_register.md`) |
| Methodology, scoring and sensitivity design | Done, written before any results (`docs/methodology_and_scoring.md`) |
| SQL schema + 17 business queries | Written; run on a toy fixture only (`tests/test_sql.py`) |
| Analysis library (scoring, sensitivity, K-Means, OLS, VIF, haversine, finance) | Written; 9 unit tests pass (`tests/test_analysis.py`) |
| 16 notebooks | Generated, every code cell syntax-checked; **not run: no real data yet** |
| DAX measures + Power BI model spec | Written; **not opened in Power BI** |
| Data dictionary, limitations and ethics, report templates | Done as documents; raw-column mapping pending profiling |
| Census 2011 PCA for all 24 wards loaded and reconciled to district totals | **Done** (`data/raw/pca_*_wards.csv`, `data/processed/ward_census_2011*.csv`) |
| Demographic EDA, correlations, preliminary clusters, 4 figures | **Done on real data** (`reports/phase_A_findings_and_dq.md`, `reports/figures/`) |
| Dealer layer: 85 aggregator-listed outlets (36 Maruti) assigned to wards by analyst judgement, **unverified**, no coordinates (`data/processed/dealers_aggregator_unverified.csv`, `ward_features_with_dealers.csv`) | **Preliminary** (`reports/phase_B_competition_preliminary.md`) |
| Car ownership, accessibility, rent, density, Vahan (full), affluence proxy from assets | **Not done. Data not obtainable by the build tools; user must supply** |
| Opportunity score, sensitivity, maps, finance, shortlist, recommendation | **Not done. Needs the missing layers above** |

## What blocks the rest
The build sandbox cannot reach data.opencity.in or overpass-api.de (egress policy). Download the files listed in `data/raw/DOWNLOAD_THESE_FILES.md`, put them in `data/raw/`.

## Run order once data is in place
```
python3 -I tests/test_analysis.py && python3 -I tests/test_sql.py
python3 -I src/ingest_and_profile.py data/raw reports/profile
# then notebooks 03 -> 16 in order (06 builds data/processed/ward_master.csv)
```
No result in this project may be quoted unless it came from a notebook run on the real files.

## Scenario run (assumption-based)
`src/scenario_model.py`, `scenario/`, `reports/final_illustrative_scenario_report.md`. Built on analyst-assumed tiers, **illustrative only**. Replace `data/assumptions/ward_assumed_inputs.csv` with measured data to make it real.

## Added in the final pass
`reports/management_report.md`, `reports/risk_matrix.md`, `reports/figures/06_ward_maps_approx.png` (approximate centroids in `data/assumptions/ward_centroids_approx.csv`), `scenario/approx_centroid_neighbours.csv`. The presentation is a published Slides artifact. All illustrative.

## Measured ownership update
`src/ingest_houselisting.py`, `src/real_ownership_model.py`, `src/real_score.py`, `reports/measured_ownership_report.md`, `scenario/measured_*.csv`. Car/asset ownership is now measured (Census 2011 HH-14). Cost and accessibility are still assumed tiers. Supersedes the R/N result.

## Final pass
`run_all.py` reruns the measured pipeline. `src/real_clusters.py` clusters on ownership. Maps with measured values: `reports/figures/08_ward_maps_measured.png`. The 16 template notebooks have not been run as written; the scripts above are the executed analysis.
