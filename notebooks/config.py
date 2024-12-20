import os

# DATA FOLDERS
DATA_EXTERNAL = r"../data/external"
DATA_INTERIM = r"../data/interim"
DATA_RAW = r"../data/raw"
REPORTS = r"../reports"
REPORTS_FIGURES = r"../reports/figures"

# CLUB EXPRESS DATA EXPORTS
ACTIVE_MEMBERS_EXTRA_CSV = r"ActiveMembersExtra.csv"
EVENT_INFORMATION_DATA_CSV = r"event_information_data.csv"
EVENTS_AND_REGISTRANTS_CSV = r"events_and_registrants.csv"

# EXTERNAL DATA SETS
NE_50M_ADMIN_0_COUNTRIES_ZIP = r"ne_50m_admin_0_countries.zip"
NE_50M_ADMIN_1_STATES_PROVINCES_ZIP = r"ne_50m_admin_1_states_provinces.zip"
NE_50M_POPULATED_PLACES_ZIP = r"ne_50m_populated_places.zip"

# CHARTS
CHART_CLUB_MEMBER_AGE_GENDER_DISTRIBUTION = r"club-member-age-gender-distribution.png"
CHART_CLUB_MEMBER_COUNTRY_DISTRIBUTION = r"club-member-country-distribution.png"
CHART_CLUB_MEMBER_GENDER_DISTRIBUTION = r"club-member-gender-distribution.png"

CHART_CLUB_MEMBER_MEAN_AGE_DISTRIBUTION = r"club-member-mean-age-distribution.png"
CHART_CLUB_MEMBER_MEDIAN_AGE_DISTRIBUTION = r"club-member-median-age-distribution.png"

# GENERATED DATA
SPARSE_EVENT_DATA_CSV = r"sparse_event_data.csv"

# Reports
OVERALL_ENGAGEMENT_REPORT_MD = r"club-engagement.md"

# Resolved paths
ACTIVE_MEMBERS_EXTRA_RAW = os.path.join(DATA_RAW, ACTIVE_MEMBERS_EXTRA_CSV)
ACTIVE_MEMBERS_EXTRA_INTERIM = os.path.join(DATA_INTERIM, ACTIVE_MEMBERS_EXTRA_CSV)

CLUB_MEMBER_AGE_GENDER_DISTRIBUTION = os.path.join(
    REPORTS_FIGURES, CHART_CLUB_MEMBER_AGE_GENDER_DISTRIBUTION
)
CLUB_MEMBER_COUNTRY_DISTRIBUTION = os.path.join(
    REPORTS_FIGURES, CHART_CLUB_MEMBER_COUNTRY_DISTRIBUTION
)
CLUB_MEMBER_GENDER_DISTRIBUTION = os.path.join(
    REPORTS_FIGURES, CHART_CLUB_MEMBER_GENDER_DISTRIBUTION
)

CLUB_MEMBER_MEAN_AGE_DISTRIBUTION = os.path.join(
    REPORTS_FIGURES, CHART_CLUB_MEMBER_MEAN_AGE_DISTRIBUTION
)

CLUB_MEMBER_MEDIAN_AGE_DISTRIBUTION = os.path.join(
    REPORTS_FIGURES, CHART_CLUB_MEMBER_MEDIAN_AGE_DISTRIBUTION
)

EVENT_INFORMATION_DATA_RAW = os.path.join(DATA_RAW, EVENT_INFORMATION_DATA_CSV)
EVENT_INFORMATION_DATA_INTERIM = os.path.join(DATA_INTERIM, EVENT_INFORMATION_DATA_CSV)

EVENTS_AND_REGISTRANTS_RAW = os.path.join(DATA_RAW, EVENTS_AND_REGISTRANTS_CSV)
EVENTS_AND_REGISTRANTS_INTERIM = os.path.join(DATA_INTERIM, EVENTS_AND_REGISTRANTS_CSV)

SPARSE_EVENT_DATA_INTERIM = os.path.join(DATA_INTERIM, SPARSE_EVENT_DATA_CSV)

OVERALL_ENGAGEMENT_REPORT = os.path.join(REPORTS, OVERALL_ENGAGEMENT_REPORT_MD)

NE_50M_ADMIN_0_COUNTRIES = os.path.join(DATA_EXTERNAL, NE_50M_ADMIN_0_COUNTRIES_ZIP)
NE_50M_ADMIN_1_STATES_PROVINCES = os.path.join(DATA_EXTERNAL, NE_50M_ADMIN_1_STATES_PROVINCES_ZIP)
NE_50M_POPULATED_PLACES = os.path.join(DATA_EXTERNAL, NE_50M_POPULATED_PLACES_ZIP)

# Colours
CANADA_RED = "#ff0000"
GENDER_NEUTRAL = "#a280b6"
GENDER_NEUTRAL_FILL = "#d1b3d6"
GENDER_BLUE = "#1f77b4"
GENDER_PINK = "#ff69b4"
USA_BLUE = "#0000ff"
BMW_BLUE = "#0000FF"
