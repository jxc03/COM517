Column explanation:
Category - category of issue
Comment - description of specific issue
Date - when the issue was identified
Type - type of issue
Severity - level of seriousness
Priority - urgency of resolving the issue
Suggested action - recommended actions to resolve the issue
Tags - list of keywords related to the issue
Date reviewed - date of when the issue has been reiewed
Reviewer ID - reviewer ID
Reviewer details - simple details of reviewer
Resolved - Whether the issue has been resolved
Resolution date - if resolved, when
Additional Notes - 
Impact - the impact of the issue

Endpoint brief explanation:
http://127.0.0.1:2000/show_all
Shows all documents in the database without any filtering
http://127.0.0.1:2000/all_appendix 
Retrieves all documents specifically categorised as "Appendix-related concerns"
http://127.0.0.1:2000/all_MMT
Retrieves all documents categorised as "Method, Mathematics and Terminology"
http://127.0.0.1:2000/get_appendix
Gets selected fields (Category, Comment, Date, Severity, Priority, Suggested Action) for Method, Mathematics and Terminology documents
Returns filtered information rather than complete documents
http://127.0.0.1:2000/get_mmt
Gets selected fields (Category, Comment, Date, Severity, Priority, Suggested Action) for Method, Mathematics and Terminology documents
Similar to get_appendix but for MMT category
http://127.0.0.1:2000/get_math_tags
Retrieves all documents tagged with "math"
http://127.0.0.1:2000/get_mmt_severity_high
Finds documents with "method" tag, "High" severity, and "Critical" priority
Excludes ObjectID from results
http://127.0.0.1:2000/get_appendix_missingContent_tag
Retrieves documents tagged with both "appendix" and "missing content"
Returns complete documents with converted ObjectIDs
http://127.0.0.1:2000/get_doc_15th_onwards
Gets all documents dated from January 20, 2024 onwards
Returns document information including all fields
http://127.0.0.1:2000/get_editor_reviewers
Retrieves reviewer information for reviewers with the role of "editor"
Case-insensitive search
Returns only the reviewer details section
http://127.0.0.1:2000/get_important_technical_tag
Finds documents with technical tags rated importance 4 or higher
Filters to only include qualifying tags in the response
http://127.0.0.1:2000/get_specified_tag
Retrieves documents with exact matching tag specifications
Looks for specific combinations of tag name, importance, category, and date
http://127.0.0.1:2000/search
Performs text search across the collection
Requires a query parameter (?query=searchterm)
http://127.0.0.1:2000/severity_impact
Analyse the relationship between severity and impact
Provides metrics including issue counts and resolution rates
http://127.0.0.1:2000/unwind_tags
Breaks down tag information into separate documents
Provides tag analysis with related document information
http://127.0.0.1:2000/comment_word_count
Analyses word frequency in comments
Returns word counts sorted by frequency
http://127.0.0.1:2000/category_analysis
Provides  analysis of categories including tag statistics
Returns metrics like total issues, importance averages, and resolution counts
http://127.0.0.1:2000/update_priority [GET, PUT]
Updates priority to "Critical" for documents with high severity and major impact
GET: Returns error message instructing to use PUT
PUT: Performs the priority update
