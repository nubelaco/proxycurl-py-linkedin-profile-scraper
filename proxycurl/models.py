from enum import Enum, auto
from typing import Optional, List, Tuple
import sys
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class CompanyType(Enum):
    EDUCATIONAL = auto()
    GOVERNMENT_AGENCY = auto()
    NON_PROFIT = auto()
    PARTNERSHIP = auto()
    PRIVATELY_HELD = auto()
    PUBLIC_COMPANY = auto()
    SELF_EMPLOYED = auto()
    SELF_OWNED = auto()


class CompanyLocation(TypedDict):
    country: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    line_1: Optional[str]
    is_hq: bool
    state: Optional[str]


class SimilarCompany(TypedDict):
    name: Optional[str]
    link: Optional[str]
    industry: Optional[str]
    location: Optional[str]


class AffiliatedCompany(TypedDict):
    name: Optional[str]
    link: Optional[str]
    industry: Optional[str]
    location: Optional[str]


class Date(TypedDict):
    day: Optional[int]
    month: Optional[int]
    year: int


class CompanyUpdate(TypedDict):
    article_link: Optional[str]
    image: Optional[str]
    posted_on: Optional[Date]
    text: Optional[str]
    total_likes: Optional[int]


class LinkedinSchool(TypedDict):
    linkedin_internal_id: str
    description: Optional[str]
    website: Optional[str]
    industry: Optional[str]
    company_size: Tuple[int, int]
    company_size_on_linkedin: Optional[int]
    hq: Optional[CompanyLocation]
    company_type: Optional[CompanyType]
    founded_year: Optional[int]
    specialities: List[str]
    locations: CompanyLocation
    name: Optional[str]
    tagline: Optional[str]
    universal_name_id: Optional[str]
    profile_pic_url: Optional[str]
    background_cover_image_url: Optional[str]
    search_id: str
    similar_companies: SimilarCompany
    affiliated_companies: AffiliatedCompany
    updates: CompanyUpdate
    follower_count: Optional[int]


class AcquiredCompany(TypedDict):
    linkedin_profile_url: Optional[str]
    crunchbase_profile_url: Optional[str]
    announced_date: Optional[Date]
    price: Optional[int]


class Acquisitor(TypedDict):
    linkedin_profile_url: Optional[str]
    crunchbase_profile_url: Optional[str]
    announced_date: Optional[Date]
    price: Optional[int]


class Acquisition(TypedDict):
    acquired: AcquiredCompany
    acquired_by: Optional[Acquisitor]


class Exit(TypedDict):
    linkedin_profile_url: Optional[str]
    crunchbase_profile_url: Optional[str]
    name: Optional[str]


class CompanyDetails(TypedDict):
    crunchbase_profile_url: Optional[str]
    ipo_status: Optional[str]
    crunchbase_rank: Optional[int]
    founding_date: Optional[Date]
    operating_status: Optional[str]
    company_type: Optional[str]
    contact_email: Optional[str]
    phone_number: Optional[str]
    facebook_id: Optional[str]
    twitter_id: Optional[str]
    number_of_funding_rounds: Optional[int]
    total_funding_amount: Optional[int]
    stock_symbol: Optional[str]
    ipo_date: Optional[Date]
    number_of_lead_investors: Optional[int]
    number_of_investors: Optional[int]
    total_fund_raised: Optional[int]
    number_of_investments: Optional[int]
    number_of_lead_investments: Optional[int]
    number_of_exits: Optional[int]
    number_of_acquisitions: Optional[int]


class Investor(TypedDict):
    linkedin_profile_url: Optional[str]
    name: Optional[str]
    type: Optional[str]


class Funding(TypedDict):
    funding_type: Optional[str]
    money_raised: Optional[int]
    announced_date: Optional[Date]
    number_of_investor: Optional[int]
    investor_list: Optional[Investor]


class LinkedinCompany(TypedDict):
    linkedin_internal_id: str
    description: Optional[str]
    website: Optional[str]
    industry: Optional[str]
    company_size: Tuple[int, int]
    company_size_on_linkedin: Optional[int]
    hq: Optional[CompanyLocation]
    company_type: Optional[CompanyType]
    founded_year: Optional[int]
    specialities: List[str]
    locations: CompanyLocation
    name: Optional[str]
    tagline: Optional[str]
    universal_name_id: Optional[str]
    profile_pic_url: Optional[str]
    background_cover_image_url: Optional[str]
    search_id: str
    similar_companies: SimilarCompany
    affiliated_companies: AffiliatedCompany
    updates: CompanyUpdate
    follower_count: Optional[int]
    acquisitions: Optional[Acquisition]
    exit_data: Optional[Exit]
    extra: Optional[CompanyDetails]
    funding_data: Optional[Funding]
    categories: Optional[List[str]]
    customer_list: Optional[List[str]]


class Experience(TypedDict):
    starts_at: Optional[Date]
    ends_at: Optional[Date]
    company: Optional[str]
    company_linkedin_profile_url: Optional[str]
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    logo_url: Optional[str]


class Education(TypedDict):
    starts_at: Optional[Date]
    ends_at: Optional[Date]
    field_of_study: Optional[str]
    degree_name: Optional[str]
    school: Optional[str]
    school_linkedin_profile_url: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]
    grade: str
    activities_and_societies: str


class AccomplishmentOrg(TypedDict):
    starts_at: Optional[Date]
    ends_at: Optional[Date]
    org_name: Optional[str]
    title: Optional[str]
    description: Optional[str]


class Publication(TypedDict):
    name: Optional[str]
    publisher: Optional[str]
    published_on: Optional[Date]
    description: Optional[str]
    url: Optional[str]


class HonourAward(TypedDict):
    title: Optional[str]
    issuer: Optional[str]
    issued_on: Optional[Date]
    description: Optional[str]


class Patent(TypedDict):
    title: Optional[str]
    issuer: Optional[str]
    issued_on: Optional[Date]
    description: Optional[str]
    application_number: Optional[str]
    patent_number: Optional[str]
    url: Optional[str]


class Course(TypedDict):
    name: Optional[str]
    number: Optional[str]


class Project(TypedDict):
    starts_at: Optional[Date]
    ends_at: Optional[Date]
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]


class TestScore(TypedDict):
    name: Optional[str]
    score: Optional[str]
    date_on: Optional[Date]
    description: Optional[str]


class VolunteeringExperience(TypedDict):
    starts_at: Optional[Date]
    ends_at: Optional[Date]
    title: Optional[str]
    cause: Optional[str]
    company: Optional[str]
    company_linkedin_profile_url: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]


class Certification(TypedDict):
    starts_at: Optional[Date]
    ends_at: Optional[Date]
    name: Optional[str]
    license_number: Optional[str]
    display_source: Optional[str]
    authority: Optional[str]
    url: Optional[str]


class PeopleAlsoViewed(TypedDict):
    link: Optional[str]
    name: Optional[str]
    summary: Optional[str]
    location: Optional[str]


class Activity(TypedDict):
    title: Optional[str]
    link: Optional[str]
    activity_status: Optional[str]


class SimilarProfile(TypedDict):
    name: Optional[str]
    link: Optional[str]
    summary: Optional[str]
    location: Optional[str]


class Article(TypedDict):
    title: Optional[str]
    link: Optional[str]
    published_date: Optional[Date]
    author: Optional[str]
    image_url: Optional[str]


class PersonGroup(TypedDict):
    profile_pic_url: Optional[str]
    name: Optional[str]
    url: Optional[str]


class InferredSalary(TypedDict):
    min: Optional[float]
    max: Optional[float]


class PersonExtra(TypedDict):
    github_profile_id: Optional[str]
    facebook_profile_id: Optional[str]
    twitter_profile_id: Optional[str]


class PersonEndpointResponse(TypedDict):
    public_identifier: Optional[str]
    profile_pic_url: str
    background_cover_image_url: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    follower_count: int
    occupation: Optional[str]
    headline: Optional[str]
    summary: Optional[str]
    country: Optional[str]
    country_full_name: Optional[str]
    city: Optional[str]
    state: Optional[str]
    experiences: Experience
    education: Education
    languages: List[str]
    accomplishment_organisations: AccomplishmentOrg
    accomplishment_publications: Publication
    accomplishment_honors_awards: HonourAward
    accomplishment_patents: Patent
    accomplishment_courses: Course
    accomplishment_projects: Project
    accomplishment_test_scores: TestScore
    volunteer_work: VolunteeringExperience
    certifications: Certification
    connections: Optional[int]
    people_also_viewed: PeopleAlsoViewed
    recommendations: List[str]
    activities: Activity
    similarly_named_profiles: SimilarProfile
    articles: Article
    groups: PersonGroup
    skills: List[str]
    inferred_salary: Optional[InferredSalary]
    gender: Optional[str]
    birth_date: Optional[Date]
    industry: Optional[str]
    extra: Optional[PersonExtra]
    interests: List[str]
    personal_emails: List[str]
    personal_numbers: List[str]


class CompanyCustomer(TypedDict):
    linkedin_company_profile_url: str
    twitter_profile_url: Optional[str]
    email: Optional[str]


class CustomerList(TypedDict):
    companies: CompanyCustomer


class CSearchResult(TypedDict):
    linkedin_profile_url: str
    profile: Optional[LinkedinCompany]
    last_updated: Optional[str]


class CompanySearchResult(TypedDict):
    results: CSearchResult
    next_page: Optional[str]
    total_result_count: int


class PublicPerson(TypedDict):
    public_identifier: Optional[str]
    profile_pic_url: str
    background_cover_image_url: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    follower_count: int
    occupation: Optional[str]
    headline: Optional[str]
    summary: Optional[str]
    country: Optional[str]
    country_full_name: Optional[str]
    city: Optional[str]
    state: Optional[str]
    experiences: Experience
    education: Education
    languages: List[str]
    accomplishment_organisations: AccomplishmentOrg
    accomplishment_publications: Publication
    accomplishment_honors_awards: HonourAward
    accomplishment_patents: Patent
    accomplishment_courses: Course
    accomplishment_projects: Project
    accomplishment_test_scores: TestScore
    volunteer_work: VolunteeringExperience
    certifications: Certification
    connections: Optional[int]
    people_also_viewed: PeopleAlsoViewed
    recommendations: List[str]
    activities: Activity
    similarly_named_profiles: SimilarProfile
    articles: Article
    groups: PersonGroup
    skills: List[str]


class Employee(TypedDict):
    profile_url: str
    profile: Optional[PublicPerson]
    last_updated: Optional[str]


class EmployeeList(TypedDict):
    employees: Employee
    next_page: Optional[str]


class EmployeeCount(TypedDict):
    total_employee: int
    linkedin_employee_count: Optional[int]
    linkdb_employee_count: int
    regression_notice: str


class ProfilePicture(TypedDict):
    tmp_profile_pic_url: str


class PersonLookupUrlEnrichResult(TypedDict):
    url: Optional[str]
    name_similarity_score: Optional[float]
    company_similarity_score: Optional[float]
    title_similarity_score: Optional[float]
    location_similarity_score: Optional[float]
    profile: PersonEndpointResponse
    last_updated: Optional[str]


class JobListEntry(TypedDict):
    company: Optional[str]
    company_url: Optional[str]
    job_title: Optional[str]
    job_url: Optional[str]
    list_date: Optional[str]
    location: Optional[str]


class JobListPage(TypedDict):
    job: JobListEntry
    next_page_no: Optional[int]
    next_page_api_url: Optional[str]
    previous_page_no: Optional[int]
    previous_page_api_url: Optional[str]


class JobListCount(TypedDict):
    count: int


class RoleSearchEnrichedResult(TypedDict):
    linkedin_profile_url: Optional[str]
    profile: PersonEndpointResponse
    last_updated: Optional[str]


class CompanyUrlEnrichResult(TypedDict):
    url: Optional[str]
    profile: LinkedinCompany
    last_updated: Optional[str]


class Student(TypedDict):
    profile_url: str
    profile: Optional[PublicPerson]
    last_updated: Optional[str]


class StudentList(TypedDict):
    students: Student
    next_page: Optional[str]


class ReverseEmailUrlEnrichResult(TypedDict):
    linkedin_profile_url: Optional[str]
    twitter_profile_url: Optional[str]
    facebook_profile_url: Optional[str]
    url: Optional[str]
    similarity_score: Optional[float]
    backwards_compatibility_notes: Optional[str]
    profile: Optional[PersonEndpointResponse]
    last_updated: Optional[str]


class ReverseContactNumberResult(TypedDict):
    linkedin_profile_url: Optional[str]
    twitter_profile_url: Optional[str]
    facebook_profile_url: Optional[str]


class ExtractionEmailResult(TypedDict):
    email_queue_count: int


class SearchResult(TypedDict):
    linkedin_profile_url: str
    profile: Optional[PublicPerson]
    last_updated: Optional[str]


class PersonSearchResult(TypedDict):
    results: SearchResult
    next_page: Optional[str]
    total_result_count: int


class JobLocation(TypedDict):
    country: Optional[str]
    region: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    street: Optional[str]


class JobCompany(TypedDict):
    name: Optional[str]
    url: Optional[str]
    logo: Optional[str]


class JobProfile(TypedDict):
    linkedin_internal_id: Optional[str]
    job_description: Optional[str]
    apply_url: Optional[str]
    title: Optional[str]
    location: JobLocation
    company: JobCompany
    seniority_level: Optional[str]
    industry: List[str]
    employment_type: Optional[str]
    job_functions: List[str]
    total_applicants: Optional[int]


class CreditBalance(TypedDict):
    credit_balance: int


class DisposableEmail(TypedDict):
    is_disposable_email: bool
    is_free_email: bool


class PersonalContactNumbers(TypedDict):
    numbers: List[str]


class PDLEmailResult(TypedDict):
    emails: List[str]
    invalid_emails: List[str]
