-- Source-aware reference retrieval, no external service required.
SELECT year,team,robot_name,epa_rank,epa,architecture FROM robot_dossiers WHERE year=2026 ORDER BY epa_rank;
SELECT d.year,d.team,d.robot_name,s.description,s.coverage_status FROM subsystems s JOIN robot_dossiers d ON d.id=s.robot_id WHERE s.subsystem='endgame' AND d.year=2026;
SELECT d.id,d.architecture FROM robot_search f JOIN robot_dossiers d ON d.id=f.robot_id WHERE robot_search MATCH 'hopper AND drum';
SELECT r.robot_id,s.url,s.review_basis,r.relationship FROM robot_sources r JOIN sources s ON s.id=r.source_id WHERE r.robot_id='2026-4414';
SELECT e.year,e.name,e.week,b.clean_score_median,b.top_pre_elim_epa,b.eighth_pre_elim_epa FROM benchmarks b JOIN events e ON e.key=b.event WHERE e.type IN ('district','district_cmp') ORDER BY e.year,e.week;
SELECT key,review_status FROM einstein_reviews WHERE json_array_length(json_extract(data_json,'$.strategic_notes'))=0;
-- Do not infer climb points from 2026 endgame_points:
SELECT key,json_extract(result_json,'$.red_endgame_fuel'),json_extract(result_json,'$.red_endgame_tower') FROM matches WHERE event='2026cmptx';

-- Long context and evidence navigation added in the expansion:
SELECT id,title,year,robot_id FROM context_documents ORDER BY year,id;
SELECT document_id,kind,snippet(context_search,2,'[',']',' … ',24) FROM context_search WHERE context_search MATCH 'hopper AND rebuild';
SELECT path,caption,source_url,review_status FROM mechanism_images WHERE robot_id='2026-4414';
SELECT created_at,author,url,navigation_tags_json,review_status FROM source_posts WHERE robot_id='2026-1768' ORDER BY created_at;
SELECT url,kind,validation FROM cad_code_links WHERE robot_id='2025-1323';
SELECT video_id,title,review_status,transcript_status FROM video_reviews WHERE review_status='unreviewed';
-- A full available transcript review is not a visual match audit.
SELECT title,source_summary,transfer_analysis,visual_review FROM video_reviews WHERE video_id='U2JrZxh6YsE';


-- Technical construction, intent and inference remain separate.
SELECT robot_id,title,construction,team_stated_reason,engineering_analysis FROM technical_mechanisms WHERE robot_id='2026-2910';
SELECT robot_id,component,published_parameters,source_url FROM technical_parameters WHERE robot_id='2025-1323';
SELECT status,count(*) FROM binder_audit GROUP BY status;
SELECT group_name,metadata_json FROM tower_summary_2026;
