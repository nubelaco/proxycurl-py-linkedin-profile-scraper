from proxycurl.config import (
    BASE_URL, PROXYCURL_API_KEY, TIMEOUT, MAX_RETRIES, MAX_BACKOFF_SECONDS
)
from proxycurl.gevent.base import ProxycurlBase
from proxycurl.models import (
    PersonEndpointResponse,
    PersonSearchResult,
    PersonLookupUrlEnrichResult,
    ReverseEmailUrlEnrichResult,
    ReverseContactNumberResult,
    ExtractionEmailResult,
    PersonalContactNumbers,
    PDLEmailResult,
    ProfilePicture,
    LinkedinCompany,
    CompanySearchResult,
    CompanyUrlEnrichResult,
    JobListPage,
    JobListCount,
    EmployeeCount,
    EmployeeList,
    RoleSearchEnrichedResult,
    LinkedinSchool,
    StudentList,
    JobProfile,
    CustomerList,
    CreditBalance,
)


class _LinkedinPerson:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        extra: str = None,
        github_profile_id: str = None,
        facebook_profile_id: str = None,
        twitter_profile_id: str = None,
        personal_contact_number: str = None,
        personal_email: str = None,
        inferred_salary: str = None,
        skills: str = None,
        use_cache: str = None,
        fallback_to_cache: str = None,
        twitter_profile_url: str = None,
        facebook_profile_url: str = None,
        linkedin_profile_url: str = None,
    ) -> PersonEndpointResponse:
        """Person Profile Endpoint
        
                Cost: 1 credit / successful request.
        Get structured data of a Personal Profile
        
        :param extra: Enriches the Person Profile with extra details from external sources.
            Extra details include gender, birth date, industry and interests.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide extra data field.
            - `include` - Append extra data to the person profile object.
            Costs an extra `1` credit on top of the cost of the base endpoint (if data is available).
        :type extra: str
        :param github_profile_id: Enriches the Person Profile with Github Id from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide Github Id data field.
            - `include` - Append Github Id data to the person profile object.
            Costs an extra `1` credit on top of the cost of the base endpoint (if data is available).
        :type github_profile_id: str
        :param facebook_profile_id: Enriches the Person Profile with Facebook Id from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide Facebook Id data field.
            - `include` - Append Facebook Id data to the person profile object.
            Costs an extra `1` credit on top of the cost of the base endpoint (if data is available).
        :type facebook_profile_id: str
        :param twitter_profile_id: Enriches the Person Profile with Twitter Id from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide Twitter Id data field.
            - `include` - Append Twitter Id data to the person profile object.
            Costs an extra `1` credit on top of the cost of the base endpoint (if data is available).
        :type twitter_profile_id: str
        :param personal_contact_number: Enriches the Person Profile with personal numbers from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide personal numbers data field.
            - `include` - Append personal numbers data to the person profile object.
            Costs an extra `1` credit per email returned on top of the cost of the base endpoint (if data is available).
        :type personal_contact_number: str
        :param personal_email: Enriches the Person Profile with personal emails from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide personal emails data field.
            - `include` - Append personal emails data to the person profile object.
            Costs an extra `1` credit per email returned on top of the cost of the base endpoint (if data is available).
        :type personal_email: str
        :param inferred_salary: Include inferred salary range from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide inferred salary data field.
            - `include` - Append inferred salary range data to the person profile object.
            Costs an extra `1` credit on top of the cost of the base endpoint (if data is available).
        :type inferred_salary: str
        :param skills: Include skills data from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide skills data field.
            - `include` - Append skills data to the person profile object.
            Costs an extra `1` credit on top of the cost of the base endpoint (if data is available).
        :type skills: str
        :param use_cache: `if-present` The default behavior.
            Fetches profile from cache regardless of age of profile.
            If profile is not available in cache, API will attempt to source profile externally.

            `if-recent` API will make a best effort to return a fresh profile no older than 29 days."
            Costs an extra `1` credit on top of the cost of the base endpoint.
        :type use_cache: str
        :param fallback_to_cache: Tweaks the fallback behavior if an error arises from fetching a fresh profile.

            This parameter accepts the following values:
            * `on-error` (default value) - Fallback to reading the profile from cache if an error arises.
            * `never` - Do not ever read profile from cache.
        :type fallback_to_cache: str
        :param twitter_profile_url:                     The Twitter Profile URL from which you wish to extract person profile

                                URL should be in the format of `https://twitter.com/<public-identifier>`

            yes (Include only one of: `linkedin_profile_url`, `twitter_profile_url`, or `facebook_profile_url`)
        :type twitter_profile_url: str
        :param facebook_profile_url:                     The Facebook Profile URL from which you wish to extract person profile

                                URL should be in the format of `https://facebook.com/<public-identifier>`

            yes (Include only one of: `linkedin_profile_url`, `twitter_profile_url`, or `facebook_profile_url`)
        :type facebook_profile_url: str
        :param linkedin_profile_url:                     The LinkedIn Profile URL from which you wish to extract person profile

                                URL should be in the format of `https://linkedin.com/in/<public-identifier>`

            yes (Include only one of: `linkedin_profile_url`, `twitter_profile_url`, or `facebook_profile_url`)
        :type linkedin_profile_url: str
        :return: An object of :class:`proxycurl.models.PersonEndpointResponse` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PersonEndpointResponse`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if extra is not None:
            params['extra'] = extra
        if github_profile_id is not None:
            params['github_profile_id'] = github_profile_id
        if facebook_profile_id is not None:
            params['facebook_profile_id'] = facebook_profile_id
        if twitter_profile_id is not None:
            params['twitter_profile_id'] = twitter_profile_id
        if personal_contact_number is not None:
            params['personal_contact_number'] = personal_contact_number
        if personal_email is not None:
            params['personal_email'] = personal_email
        if inferred_salary is not None:
            params['inferred_salary'] = inferred_salary
        if skills is not None:
            params['skills'] = skills
        if use_cache is not None:
            params['use_cache'] = use_cache
        if fallback_to_cache is not None:
            params['fallback_to_cache'] = fallback_to_cache
        if twitter_profile_url is not None:
            params['twitter_profile_url'] = twitter_profile_url
        if facebook_profile_url is not None:
            params['facebook_profile_url'] = facebook_profile_url
        if linkedin_profile_url is not None:
            params['linkedin_profile_url'] = linkedin_profile_url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/v2/linkedin',
            params=params,
            data={
            },
            result_class=PersonEndpointResponse
        )

    def search(
        self,
        country: str,
        first_name: str = None,
        last_name: str = None,
        education_field_of_study: str = None,
        education_degree_name: str = None,
        education_school_name: str = None,
        education_school_linkedin_profile_url: str = None,
        current_role_title: str = None,
        past_role_title: str = None,
        current_role_before: str = None,
        current_role_after: str = None,
        current_company_linkedin_profile_url: str = None,
        past_company_linkedin_profile_url: str = None,
        current_job_description: str = None,
        past_job_description: str = None,
        current_company_name: str = None,
        past_company_name: str = None,
        linkedin_groups: str = None,
        languages: str = None,
        region: str = None,
        city: str = None,
        headline: str = None,
        summary: str = None,
        industries: str = None,
        interests: str = None,
        skills: str = None,
        current_company_country: str = None,
        current_company_region: str = None,
        current_company_city: str = None,
        current_company_type: str = None,
        current_company_follower_count_min: str = None,
        current_company_follower_count_max: str = None,
        current_company_industry: str = None,
        current_company_employee_count_min: str = None,
        current_company_employee_count_max: str = None,
        current_company_description: str = None,
        current_company_founded_after_year: str = None,
        current_company_founded_before_year: str = None,
        current_company_funding_amount_min: str = None,
        current_company_funding_amount_max: str = None,
        current_company_funding_raised_after: str = None,
        current_company_funding_raised_before: str = None,
        public_identifier_in_list: str = None,
        public_identifier_not_in_list: str = None,
        page_size: str = None,
        enrich_profiles: str = None,
    ) -> PersonSearchResult:
        """Person Search Endpoint
        
                Cost: 35 credits / successful request base charge.
        Search for people who meet a set of criteria within our exhaustive dataset of people profiles.

        This API endpoint is powered by [LinkDB](https://nubela.co/proxycurl/linkdb), our exhaustive dataset of people and company profiles.

        This API endpoint can return at most 10,000 results per search.
        
        :param country: Filter people located in this country.
            This parameter accepts a case-insensitive [Alpha-2 ISO3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :type country: str
        :param first_name: Filter people whose first names match the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type first_name: str
        :param last_name: Filter people whose last names match the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type last_name: str
        :param education_field_of_study: Filter people with a field of study matching the provided regular expression, based on education history.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type education_field_of_study: str
        :param education_degree_name: Filter people who earned a degree matching the provided regular expression, based on education history.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type education_degree_name: str
        :param education_school_name: Filter people who have attended a school whose name matches the provided regular expression, based on education history.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type education_school_name: str
        :param education_school_linkedin_profile_url: Filter people who have attended a school with a specific LinkedIn profile URL, based on education history.

            The default value of this parameter is `null`.
        :type education_school_linkedin_profile_url: str
        :param current_role_title: Filter people who are **currently** working as a role whose title matches the provided regular expression. You'll be looking for profiles on [LinkDB](https://nubela.co/proxycurl/linkdb) that show a person's current job. However, keep in mind that some of these profiles may not be up-to-date, which means you might sometimes see a person's old job instead of their current job on LinkedIn.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type current_role_title: str
        :param past_role_title: Filter people who have **in the past** worked as a role whose title matches the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type past_role_title: str
        :param current_role_before: Filter people who started their current role **before** this date. You'll be looking for profiles on [LinkDB](https://nubela.co/proxycurl/linkdb) that show a person's current job. However, keep in mind that some of these profiles may not be up-to-date, which means you might sometimes see a person's old job instead of their current job on LinkedIn.

            This parameter takes a ISO8601 date. Default value of this parameter is `null`.
        :type current_role_before: str
        :param current_role_after: Filter people who started their current role **after** this date. You'll be looking for profiles on [LinkDB](https://nubela.co/proxycurl/linkdb) that show a person's current job. However, keep in mind that some of these profiles may not be up-to-date, which means you might sometimes see a person's old job instead of their current job on LinkedIn.

            This parameter takes a ISO8601 date. Default value of this parameter is `null`.
        :type current_role_after: str
        :param current_company_linkedin_profile_url: Filter people who are **currently** working at a company represented by this LinkedIn Company Profile URL.

            Default value of this parameter is `null`.
        :type current_company_linkedin_profile_url: str
        :param past_company_linkedin_profile_url: Filter people who have **in the past** worked at the company represented by this LinkedIn Company Profile URL.

            This parameter takes a LinkedIn Company Profile URL. Default value of this parameter is `null`.
        :type past_company_linkedin_profile_url: str
        :param current_job_description: Filter people with **current** job descriptions matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type current_job_description: str
        :param past_job_description: Filter people with **past** job descriptions matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type past_job_description: str
        :param current_company_name: Filter people who are **currently** working at a company whose name matches the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type current_company_name: str
        :param past_company_name: Filter people who **have previously** worked at a company whose name matches the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type past_company_name: str
        :param linkedin_groups: Filter people who are members of LinkedIn groups whose names match the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type linkedin_groups: str
        :param languages: Filter people who list a language matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type languages: str
        :param region: Filter people located in a region matching the provided regular expression.
            A “region” in this context means “state,” “province,” or similar political division, depending on what country you’re querying.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type region: str
        :param city: Filter people located in a city matching the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type city: str
        :param headline: Filter people whose LinkedIn headline fields match the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type headline: str
        :param summary: Filter people whose LinkedIn summary fields match the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type summary: str
        :param industries: Person's inferred industry. May sometimes exist when `current_company_industry` does not, but `current_company_industry` should be preferred when it exists.
        :type industries: str
        :param interests: Filter people whose Linkedin interest fields match the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type interests: str
        :param skills: Filter people whose Linkedin skill fields match the provided regular expression.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
        :type skills: str
        :param current_company_country: Filter people who are currently working at a company with an office based in this country.

            This parameter accepts a case-insensitive [Alpha-2 ISO3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :type current_company_country: str
        :param current_company_region: Filter people who are currently working at a company based in a region matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type current_company_region: str
        :param current_company_city: Filter people who are currently working at a company based in a city matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type current_company_city: str
        :param current_company_type: Filter people who are currently working at a company of the provided LinkedIn type.

            Possible values:

            * `EDUCATIONAL`: Educational Institution
            * `GOVERNMENT_AGENCY`: Government Agency
            * `NON_PROFIT` : Nonprofit
            * `PARTNERSHIP` : Partnership
            * `PRIVATELY_HELD` : Privately Held
            * `PUBLIC_COMPANY` : Public Company
            * `SELF_EMPLOYED` : Self-Employed
            * `SELF_OWNED` : Sole Proprietorship
        :type current_company_type: str
        :param current_company_follower_count_min: Filter people who are currently working at a company with a LinkedIn follower count **more than** this value.
        :type current_company_follower_count_min: str
        :param current_company_follower_count_max: Filter people who are currently working at a company with a LinkedIn follower count **less than** this value.
        :type current_company_follower_count_max: str
        :param current_company_industry: Filter people who are currently working at a company belonging to an `industry` that matches the provided regular expression. The `industry` attribute, found in a LinkedIn Company profile, describes the industry in which the company operates. The value of this attribute is an enumerator. [This CSV file provides an exhaustive list of possible values for this attribute](https://drive.google.com/file/d/12yvYLuru7CRv3wKOIkHs5Ldocz31gJSS/view?usp=share_link).

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type current_company_industry: str
        :param current_company_employee_count_min: Filter people who are currently working at a company with **at least** this many employees.
        :type current_company_employee_count_min: str
        :param current_company_employee_count_max: Filter people who are currently working at a company with **at most** this many employees.
        :type current_company_employee_count_max: str
        :param current_company_description: Filter people who are currently working at a company with a description matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type current_company_description: str
        :param current_company_founded_after_year: Filter people who are currently working at a company that was founded **after** this year.
        :type current_company_founded_after_year: str
        :param current_company_founded_before_year: Filter people who are currently working at a company that was founded **before** this year.
        :type current_company_founded_before_year: str
        :param current_company_funding_amount_min: Filter people who are currently working at a company that has raised **at least** this much (USD) funding amount.
        :type current_company_funding_amount_min: str
        :param current_company_funding_amount_max: Filter people who are currently working at a company that has raised **at most** this much (USD) funding amount.
        :type current_company_funding_amount_max: str
        :param current_company_funding_raised_after: Filter people who are currently working at a company that has raised funding **after** this date.
        :type current_company_funding_raised_after: str
        :param current_company_funding_raised_before: Filter people who are currently working at a company that has raised funding **before** this date.
        :type current_company_funding_raised_before: str
        :param public_identifier_in_list: A list of public identifiers (the identifying portion of the person’s profile URL).
            The target person’s identifier must be a member of this list.
        :type public_identifier_in_list: str
        :param public_identifier_not_in_list: A list of public identifiers (the identifying portion of the person’s profile URL).
            The target person’s identifier must **not** be a member of this list.
        :type public_identifier_not_in_list: str
        :param page_size: Tune the maximum results returned per API call.

            The default value of this parameter is `100`.

            Accepted values for this parameter is an integer ranging from `1` to `100`.

            When `enrich_profiles=enrich`, this parameter accepts value ranging from `1` to `10`.
        :type page_size: str
        :param enrich_profiles: Get the person's complete profile data rather than just the URLs to their LinkedIn profiles.

            Each request respond with a streaming response of profiles.

            The valid values are:

            * `skip` (default): lists person's profile url only
            * `enrich`: include person's profile data in the list

            Calling this API endpoint with this parameter would add `1` credit per result returned.
        :type enrich_profiles: str
        :return: An object of :class:`proxycurl.models.PersonSearchResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PersonSearchResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['country'] = country
        if first_name is not None:
            params['first_name'] = first_name
        if last_name is not None:
            params['last_name'] = last_name
        if education_field_of_study is not None:
            params['education_field_of_study'] = education_field_of_study
        if education_degree_name is not None:
            params['education_degree_name'] = education_degree_name
        if education_school_name is not None:
            params['education_school_name'] = education_school_name
        if education_school_linkedin_profile_url is not None:
            params['education_school_linkedin_profile_url'] = education_school_linkedin_profile_url
        if current_role_title is not None:
            params['current_role_title'] = current_role_title
        if past_role_title is not None:
            params['past_role_title'] = past_role_title
        if current_role_before is not None:
            params['current_role_before'] = current_role_before
        if current_role_after is not None:
            params['current_role_after'] = current_role_after
        if current_company_linkedin_profile_url is not None:
            params['current_company_linkedin_profile_url'] = current_company_linkedin_profile_url
        if past_company_linkedin_profile_url is not None:
            params['past_company_linkedin_profile_url'] = past_company_linkedin_profile_url
        if current_job_description is not None:
            params['current_job_description'] = current_job_description
        if past_job_description is not None:
            params['past_job_description'] = past_job_description
        if current_company_name is not None:
            params['current_company_name'] = current_company_name
        if past_company_name is not None:
            params['past_company_name'] = past_company_name
        if linkedin_groups is not None:
            params['linkedin_groups'] = linkedin_groups
        if languages is not None:
            params['languages'] = languages
        if region is not None:
            params['region'] = region
        if city is not None:
            params['city'] = city
        if headline is not None:
            params['headline'] = headline
        if summary is not None:
            params['summary'] = summary
        if industries is not None:
            params['industries'] = industries
        if interests is not None:
            params['interests'] = interests
        if skills is not None:
            params['skills'] = skills
        if current_company_country is not None:
            params['current_company_country'] = current_company_country
        if current_company_region is not None:
            params['current_company_region'] = current_company_region
        if current_company_city is not None:
            params['current_company_city'] = current_company_city
        if current_company_type is not None:
            params['current_company_type'] = current_company_type
        if current_company_follower_count_min is not None:
            params['current_company_follower_count_min'] = current_company_follower_count_min
        if current_company_follower_count_max is not None:
            params['current_company_follower_count_max'] = current_company_follower_count_max
        if current_company_industry is not None:
            params['current_company_industry'] = current_company_industry
        if current_company_employee_count_min is not None:
            params['current_company_employee_count_min'] = current_company_employee_count_min
        if current_company_employee_count_max is not None:
            params['current_company_employee_count_max'] = current_company_employee_count_max
        if current_company_description is not None:
            params['current_company_description'] = current_company_description
        if current_company_founded_after_year is not None:
            params['current_company_founded_after_year'] = current_company_founded_after_year
        if current_company_founded_before_year is not None:
            params['current_company_founded_before_year'] = current_company_founded_before_year
        if current_company_funding_amount_min is not None:
            params['current_company_funding_amount_min'] = current_company_funding_amount_min
        if current_company_funding_amount_max is not None:
            params['current_company_funding_amount_max'] = current_company_funding_amount_max
        if current_company_funding_raised_after is not None:
            params['current_company_funding_raised_after'] = current_company_funding_raised_after
        if current_company_funding_raised_before is not None:
            params['current_company_funding_raised_before'] = current_company_funding_raised_before
        if public_identifier_in_list is not None:
            params['public_identifier_in_list'] = public_identifier_in_list
        if public_identifier_not_in_list is not None:
            params['public_identifier_not_in_list'] = public_identifier_not_in_list
        if page_size is not None:
            params['page_size'] = page_size
        if enrich_profiles is not None:
            params['enrich_profiles'] = enrich_profiles

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/search/person',
            params=params,
            data={
            },
            result_class=PersonSearchResult
        )

    def resolve(
        self,
        first_name: str,
        company_domain: str,
        similarity_checks: str = None,
        enrich_profile: str = None,
        location: str = None,
        title: str = None,
        last_name: str = None,
    ) -> PersonLookupUrlEnrichResult:
        """Person Lookup Endpoint
        
                Cost: 2 credits / successful request.
        Look up a person with a name and company information.
        
        :param first_name: First name of the user
        :type first_name: str
        :param company_domain: Company name or domain
        :type company_domain: str
        :param similarity_checks: Controls whether the API endpoint performs
            similarity comparisons between the input parameters
            and the results or simply returns the closest match.
            For instance, if you are searching for a person named
            "Ben Chad", and the closest result we have is "Chavvy
            Plum", our similarity checks will discard the obviously
            incorrect result and return `null` instead of a false
            positive.

            Include similarity checks to eliminate false positives.
            However, be aware that this might yield fewer results
            as false positives are discarded. Credits will still be
            deducted even if we return `null`.

            You can choose to skip similarity checks, in which
            case no credits will be charged if we return `null`.

            This parameter accepts the following values:
            * `include` (default) - Perform similarity checks and
            discard false positives. Credits will be deducted even
            if we return null .
            * `skip` - Bypass similarity checks. No credits will be
            deducted if no results are returned.
        :type similarity_checks: str
        :param enrich_profile: Enrich the result with a cached profile of the lookup result.

            The valid values are:

            * `skip` (default): do not enrich the results with cached profile data
            * `enrich`: enriches the result with cached profile data

            Calling this API endpoint with this parameter would add 1 credit.

            If you require [fresh profile data](https://nubela.co/blog/how-fresh-are-profiles-returned-by-proxycurl-api/),
            please chain this API call with the [People Profile Endpoint](https://nubela.co/proxycurl/docs#people-api-person-profile-endpoint) with the `use_cache=if-recent` parameter.
        :type enrich_profile: str
        :param location: The location of this user.

            Name of country, city or state.
        :type location: str
        :param title: Title that user is holding at his/her current job
        :type title: str
        :param last_name: Last name of the user
        :type last_name: str
        :return: An object of :class:`proxycurl.models.PersonLookupUrlEnrichResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PersonLookupUrlEnrichResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['first_name'] = first_name
        params['company_domain'] = company_domain
        if similarity_checks is not None:
            params['similarity_checks'] = similarity_checks
        if enrich_profile is not None:
            params['enrich_profile'] = enrich_profile
        if location is not None:
            params['location'] = location
        if title is not None:
            params['title'] = title
        if last_name is not None:
            params['last_name'] = last_name

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/profile/resolve',
            params=params,
            data={
            },
            result_class=PersonLookupUrlEnrichResult
        )

    def resolve_by_email(
        self,
        email: str,
        lookup_depth: str,
        enrich_profile: str = None,
    ) -> ReverseEmailUrlEnrichResult:
        """Reverse Email Lookup Endpoint
        
                Cost: 3 credits / successful request.
        Resolve social media profiles correlated from an email address.
        This API endpoint works with both personal and work emails.
        
        :param email: Email address of the user you want to look up.
        :type email: str
        :param lookup_depth: This parameter describes the depth options for our API lookup function. This endpoint can execute either a superficial or a deep lookup.

            A **superficial lookup** involves comparing the provided email with entries in our database. This approach tends to yield fewer results and is typically less effective for work-related email addresses. However, it does not consume any credits if no results are returned.

            On the other hand, a **deep lookup** extends beyond our database to utilize advanced heuristics and identify the individual associated with a given email. This method is particularly recommended for work emails.

            Please note the following valid values for the depth of the lookup:

            * `superficial`: No credits are consumed if no results are found.
            * `deep` (default): Credits are used regardless of whether any results are returned.
        :type lookup_depth: str
        :param enrich_profile: Enrich the result with a cached LinkedIn profile of the LinkedIn Profile URL result (if any).

            Valid values are:

            * `skip` (default): do not enrich the results with cached profile data.
            * `enrich`: enriches the result with cached profile data. 

            Calling this API endpoint with this parameter would add `1` additional credit.

            If you require [fresh profile data](https://nubela.co/blog/how-fresh-are-profiles-returned-by-proxycurl-api/),  please chain this API call with the `linkedin_profile_url` result with the [Person Profile Endpoint](https://nubela.co/proxycurl/docs#people-api-person-profile-endpoint) with the `use_cache=if-recent` parameter.
        :type enrich_profile: str
        :return: An object of :class:`proxycurl.models.ReverseEmailUrlEnrichResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.ReverseEmailUrlEnrichResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['email'] = email
        params['lookup_depth'] = lookup_depth
        if enrich_profile is not None:
            params['enrich_profile'] = enrich_profile

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/profile/resolve/email',
            params=params,
            data={
            },
            result_class=ReverseEmailUrlEnrichResult
        )

    def resolve_by_phone(
        self,
        phone_number: str,
    ) -> ReverseContactNumberResult:
        """Reverse Contact Number Lookup Endpoint
        
                Cost: 3 credits / successful request.
        Find social media profiles from a contact phone number.
        
        :param phone_number: [E.164 formatted](https://www.twilio.com/docs/glossary/what-e164) phone number of the person you want to identify social media profiles of.
        :type phone_number: str
        :return: An object of :class:`proxycurl.models.ReverseContactNumberResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.ReverseContactNumberResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['phone_number'] = phone_number

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/resolve/phone',
            params=params,
            data={
            },
            result_class=ReverseContactNumberResult
        )

    def lookup_email(
        self,
        linkedin_profile_url: str,
        callback_url: str = None,
    ) -> ExtractionEmailResult:
        """Work Email Lookup Endpoint
        
                Cost: 3 credits / request.
        Lookup work email address of a LinkedIn Person Profile.

        Email addresses returned are verified to not be role-based or catch-all emails. Email addresses
        returned by our API endpoint come with a 95+% deliverability guarantee

        **Endpoint behavior**

        *This endpoint* **_may not_** *return results immediately.*

        If you provided a webhook in your request parameter, our application will call your webhook with
        the result once. See `Webhook request` below.
        
        :param linkedin_profile_url: Linkedin Profile URL of the person you want to
            extract work email address from.
        :type linkedin_profile_url: str
        :param callback_url: Webhook to notify your application when
            the request has finished processing.
        :type callback_url: str
        :return: An object of :class:`proxycurl.models.ExtractionEmailResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.ExtractionEmailResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['linkedin_profile_url'] = linkedin_profile_url
        if callback_url is not None:
            params['callback_url'] = callback_url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/profile/email',
            params=params,
            data={
            },
            result_class=ExtractionEmailResult
        )

    def personal_contact(
        self,
        page_size: str = None,
        twitter_profile_url: str = None,
        facebook_profile_url: str = None,
        linkedin_profile_url: str = None,
    ) -> PersonalContactNumbers:
        """Personal Contact Number Lookup Endpoint
        
                Cost: 1 credit / contact number returned.
        Find personal phone numbers associated with a given social media profile.
        
        :param page_size: This controls the maximum number of numbers returned per API call.
            It's useful for limiting credit consumption as the number of numbers
            per identity can vary. The default value is 0, meaning there's no limit
            to the number of returned results.
        :type page_size: str
        :param twitter_profile_url: The Twitter Profile URL from which you wish to extract personal
            contact numbers


            Yes (Include only one of: `linkedin_profile_url`,
            `twitter_profile_url`, or `facebook_profile_url`)
        :type twitter_profile_url: str
        :param facebook_profile_url: The Facebook Profile URL from which you wish to extract personal
            contact numbers


            Yes (Include only one of: `linkedin_profile_url`,
            `twitter_profile_url`, or `facebook_profile_url`)
        :type facebook_profile_url: str
        :param linkedin_profile_url: The LinkedIn Profile URL from which you wish to extract personal
            contact numbers


            Yes (Include only one of: `linkedin_profile_url`,
            `twitter_profile_url`, or `facebook_profile_url`)
        :type linkedin_profile_url: str
        :return: An object of :class:`proxycurl.models.PersonalContactNumbers` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PersonalContactNumbers`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if page_size is not None:
            params['page_size'] = page_size
        if twitter_profile_url is not None:
            params['twitter_profile_url'] = twitter_profile_url
        if facebook_profile_url is not None:
            params['facebook_profile_url'] = facebook_profile_url
        if linkedin_profile_url is not None:
            params['linkedin_profile_url'] = linkedin_profile_url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/contact-api/personal-contact',
            params=params,
            data={
            },
            result_class=PersonalContactNumbers
        )

    def personal_email(
        self,
        email_validation: str = None,
        page_size: int = None,
        twitter_profile_url: str = None,
        facebook_profile_url: str = None,
        linkedin_profile_url: str = None,
    ) -> PDLEmailResult:
        """Personal Email Lookup Endpoint
        
                Cost: 1 credit / email returned.
        Find personal email addresses associated with a given social media profile.
        
        :param email_validation: How to validate each email.

            Takes the following values:
             * `none` (default) - Do not perform email validation.
             * `fast` - Perform fast email validation (does not cost extra credit).
             * `precise` - Perform deliverability validation (costs 1 extra credit per email found).

            For backward-compatibility these are also accepted:
             * `include` - Equivalent to `precise`
             * `exclude` - Equivalent to `none`
        :type email_validation: str
        :param page_size: This controls the maximum number of emails returned per API call. It's useful for limiting credit consumption as the number of emails per identity can vary. The default value is `0`, meaning there's no limit to the number of returned results.
        :type page_size: int
        :param twitter_profile_url: The Twitter Profile URL from which you wish to extract personal email addresses.
            yes (Include only one of: `linkedin_profile_url`, `twitter_profile_url`, or `facebook_profile_url`)
        :type twitter_profile_url: str
        :param facebook_profile_url: The Facebook Profile URL from which you wish to extract personal email addresses.
            yes (Include only one of: `linkedin_profile_url`, `twitter_profile_url`, or `facebook_profile_url`)
        :type facebook_profile_url: str
        :param linkedin_profile_url: The LinkedIn Profile URL from which you wish to extract personal email addresses.
            yes (Include only one of: `linkedin_profile_url`, `twitter_profile_url`, or `facebook_profile_url`)
        :type linkedin_profile_url: str
        :return: An object of :class:`proxycurl.models.PDLEmailResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PDLEmailResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if email_validation is not None:
            params['email_validation'] = email_validation
        if page_size is not None:
            params['page_size'] = page_size
        if twitter_profile_url is not None:
            params['twitter_profile_url'] = twitter_profile_url
        if facebook_profile_url is not None:
            params['facebook_profile_url'] = facebook_profile_url
        if linkedin_profile_url is not None:
            params['linkedin_profile_url'] = linkedin_profile_url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/contact-api/personal-email',
            params=params,
            data={
            },
            result_class=PDLEmailResult
        )

    def profile_picture(
        self,
        linkedin_person_profile_url: str,
    ) -> ProfilePicture:
        """Person Profile Picture Endpoint
        
                Cost: 0 credit / successful request.
        Get the profile picture of a person.

        Profile pictures are served from cached people profiles found within [LinkDB](https://nubela.co/proxycurl/linkdb).
        If the profile does not exist within [LinkDB](https://nubela.co/proxycurl/linkdb), then the API will return a `404` status code.
        
        :param linkedin_person_profile_url: LinkedIn Profile URL of the person that you are trying to get the profile picture of.
        :type linkedin_person_profile_url: str
        :return: An object of :class:`proxycurl.models.ProfilePicture` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.ProfilePicture`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['linkedin_person_profile_url'] = linkedin_person_profile_url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/person/profile-picture',
            params=params,
            data={
            },
            result_class=ProfilePicture
        )


class _LinkedinCompany:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
        resolve_numeric_id: str = None,
        categories: str = None,
        funding_data: str = None,
        extra: str = None,
        exit_data: str = None,
        acquisitions: str = None,
        use_cache: str = None,
    ) -> LinkedinCompany:
        """Company Profile Endpoint
        
                Cost: 1 credit / successful request.
        Get structured data of a Company Profile
        
        :param url: URL of the LinkedIn Company Profile to crawl.

            URL should be in the format of `https://www.linkedin.com/company/<public_identifier>`
        :type url: str
        :param resolve_numeric_id: Enable support for Company Profile URLs with numerical IDs that you most frequently fetch from Sales Navigator.
            We achieve this by resolving numerical IDs into vanity IDs with cached company profiles from [LinkDB](https://nubela.co/proxycurl/linkdb).
            For example, we will turn `https://www.linkedin.com/company/1234567890` to `https://www.linkedin.com/company/acme-corp` -- for which the API endpoint only supports the latter.

            This parameter accepts the following values:
            - `false` - Will not resolve numerical IDs.
            - `true` (default value) - Enable support for Company Profile URLs with numerical IDs.
            Costs an extra `2` credit on top of the base cost of the endpoint.
        :type resolve_numeric_id: str
        :param categories: Appends categories data of this company.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these categories (if available) for `1` extra credit.
        :type categories: str
        :param funding_data: Returns a list of funding rounds that this company has received.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these categories (if available) for `1` extra credit.
        :type funding_data: str
        :param extra: Enriches the Company Profile with extra details from external sources.
            Details include Crunchbase ranking, contact email, phone number, Facebook account, Twitter account, funding rounds and amount, IPO status, investor information, etc.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these extra details (if available) for `1` extra credit.
        :type extra: str
        :param exit_data: Returns a list of investment portfolio exits.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these categories (if available) for `1` extra credit.
        :type exit_data: str
        :param acquisitions: Provides further enriched data on acquisitions made by this company from external sources.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these acquisition data (if available) for `1` extra credit.
        :type acquisitions: str
        :param use_cache: `if-present` The default behavior. Fetches profile from cache regardless of age of profile. If profile is not available in cache, API will attempt to source profile externally.

            `if-recent` API will make a best effort to return a fresh profile no older than 29 days.Costs an extra `1` credit on top of the cost of the base endpoint.
        :type use_cache: str
        :return: An object of :class:`proxycurl.models.LinkedinCompany` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.LinkedinCompany`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['url'] = url
        if resolve_numeric_id is not None:
            params['resolve_numeric_id'] = resolve_numeric_id
        if categories is not None:
            params['categories'] = categories
        if funding_data is not None:
            params['funding_data'] = funding_data
        if extra is not None:
            params['extra'] = extra
        if exit_data is not None:
            params['exit_data'] = exit_data
        if acquisitions is not None:
            params['acquisitions'] = acquisitions
        if use_cache is not None:
            params['use_cache'] = use_cache

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company',
            params=params,
            data={
            },
            result_class=LinkedinCompany
        )

    def search(
        self,
        public_identifier_not_in_list: str = None,
        public_identifier_in_list: str = None,
        enrich_profiles: str = None,
        page_size: str = None,
        funding_raised_before: str = None,
        funding_raised_after: str = None,
        funding_amount_min: str = None,
        funding_amount_max: str = None,
        founded_before_year: str = None,
        founded_after_year: str = None,
        description: str = None,
        employee_count_min: str = None,
        employee_count_max: str = None,
        industry: str = None,
        name: str = None,
        follower_count_max: str = None,
        follower_count_min: str = None,
        type: str = None,
        city: str = None,
        region: str = None,
        country: str = None,
    ) -> CompanySearchResult:
        """Company Search Endpoint
        
                Cost: 35 credits / successful request base charge.
        Search for companies that meet a set of criteria within
            our exhaustive dataset of company profiles.

            This API endpoint is powered by [LinkDB](https://nubela.co/proxycurl/linkdb), our exhaustive dataset of company profiles.

            This API endpoint can return at most of 10,000 results per search.
        
        :param public_identifier_not_in_list: A list of public identifiers (the identifying portion of the company’s profile URL).
            The target company’s identifier must **not** be a member of this list.
        :type public_identifier_not_in_list: str
        :param public_identifier_in_list: A list of public identifiers (the identifying portion of the company’s profile URL).
            The target company’s identifier must be a member of this list.
        :type public_identifier_in_list: str
        :param enrich_profiles: Get the company's complete profile data rather than just the URLs to their LinkedIn profiles.

            Each request respond with a streaming response of profiles.

            The valid values are:

            - skip (default): lists company's profile url
            - enrich: include company's profile data in the list

            Calling this API endpoint with this parameter would add 1 credit per result returned.
        :type enrich_profiles: str
        :param page_size: Tune the maximum results returned per API call.

            The default value of this parameter is 100.

            Accepted values for this parameter is an integer ranging from 1 to 100.

            When `enrich_profiles=enrich`, this parameter accepts value ranging from `1` to `10`.
        :type page_size: str
        :param funding_raised_before: Filter companies that have raised funding **before** this date.
        :type funding_raised_before: str
        :param funding_raised_after: Filter companies that have raised funding **after** this date.
        :type funding_raised_after: str
        :param funding_amount_min: Filter companies that have raised **at least** this much (USD) funding amount.
        :type funding_amount_min: str
        :param funding_amount_max: Filter companies that have raised **at most** this much (USD) funding amount.
        :type funding_amount_max: str
        :param founded_before_year: Filter companies that were founded **before** this year.
        :type founded_before_year: str
        :param founded_after_year: Filter companies that were founded **after** this year.
        :type founded_after_year: str
        :param description: Filter companies with a description matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type description: str
        :param employee_count_min: Filter companies with **at least** this many employees.
        :type employee_count_min: str
        :param employee_count_max: Filter companies with **at most** this many employees.
        :type employee_count_max: str
        :param industry: Use this parameter to filter companies belonging to an `industry` that matches the provided regular expression. The `industry` attribute, found in a LinkedIn Company profile, describes the industry in which the company operates. The value of this attribute is an enumerator. [This CSV file provides an exhaustive list of possible values for this attribute](https://drive.google.com/file/d/12yvYLuru7CRv3wKOIkHs5Ldocz31gJSS/view?usp=share_link).

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag. The default value of this parameter is `null`.
        :type industry: str
        :param name: Filter companies with a name matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type name: str
        :param follower_count_max: Filter companies with a LinkedIn follower count **less than** this value.
        :type follower_count_max: str
        :param follower_count_min: Filter companies with a LinkedIn follower count **more than** this value.
        :type follower_count_min: str
        :param type: Filter companies of the provided LinkedIn type.

            Possible values:

            * `EDUCATIONAL`: Educational Institution
            * `GOVERNMENT_AGENCY`: Government Agency
            * `NON_PROFIT` : Nonprofit
            * `PARTNERSHIP` : Partnership
            * `PRIVATELY_HELD` : Privately Held
            * `PUBLIC_COMPANY` : Public Company
            * `SELF_EMPLOYED` : Self-Employed
            * `SELF_OWNED` : Sole Proprietorship
        :type type: str
        :param city: Filter companies based in cities matching the provided regular expression.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type city: str
        :param region: Filter companies based in regions matching the provided regular expression.
            A “region” in this context means “state,” “province,” or similar political division, depending on what country you’re querying.

            The accepted value for this parameter is a regular expression which is **case sensitive** by default and accepts an `(?i)` flag.
            The default value of this parameter is null.
        :type region: str
        :param country: Filter companies with an office based in this country.

            This parameter accepts a case-insensitive [Alpha-2 ISO3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :type country: str
        :return: An object of :class:`proxycurl.models.CompanySearchResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.CompanySearchResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if public_identifier_not_in_list is not None:
            params['public_identifier_not_in_list'] = public_identifier_not_in_list
        if public_identifier_in_list is not None:
            params['public_identifier_in_list'] = public_identifier_in_list
        if enrich_profiles is not None:
            params['enrich_profiles'] = enrich_profiles
        if page_size is not None:
            params['page_size'] = page_size
        if funding_raised_before is not None:
            params['funding_raised_before'] = funding_raised_before
        if funding_raised_after is not None:
            params['funding_raised_after'] = funding_raised_after
        if funding_amount_min is not None:
            params['funding_amount_min'] = funding_amount_min
        if funding_amount_max is not None:
            params['funding_amount_max'] = funding_amount_max
        if founded_before_year is not None:
            params['founded_before_year'] = founded_before_year
        if founded_after_year is not None:
            params['founded_after_year'] = founded_after_year
        if description is not None:
            params['description'] = description
        if employee_count_min is not None:
            params['employee_count_min'] = employee_count_min
        if employee_count_max is not None:
            params['employee_count_max'] = employee_count_max
        if industry is not None:
            params['industry'] = industry
        if name is not None:
            params['name'] = name
        if follower_count_max is not None:
            params['follower_count_max'] = follower_count_max
        if follower_count_min is not None:
            params['follower_count_min'] = follower_count_min
        if type is not None:
            params['type'] = type
        if city is not None:
            params['city'] = city
        if region is not None:
            params['region'] = region
        if country is not None:
            params['country'] = country

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/search/company',
            params=params,
            data={
            },
            result_class=CompanySearchResult
        )

    def resolve(
        self,
        company_location: str = None,
        company_domain: str = None,
        company_name: str = None,
        enrich_profile: str = None,
    ) -> CompanyUrlEnrichResult:
        """Company Lookup Endpoint
        
                Cost: 2 credits / successful request.
        Resolve Company LinkedIn Profile from company name,
            domain name and location.
        
        :param company_location: The location / region of company.
            ISO 3166-1 alpha-2 codes
        :type company_location: str
        :param company_domain: Company website or Company domain
            Requires either `company_domain` or `company_name`
        :type company_domain: str
        :param company_name: Company Name
            Requires either `company_domain` or `company_name`
        :type company_name: str
        :param enrich_profile: Enrich the result with a cached profile of the lookup result.

            The valid values are:

            * `skip` (default): do not enrich the results with cached profile data
            * `enrich`: enriches the result with cached profile data

            Calling this API endpoint with this parameter would add 1 credit.

            If you require [fresh profile data](https://nubela.co/blog/how-fresh-are-profiles-returned-by-proxycurl-api/),
            please chain this API call with the [Company Profile Endpoint](https://nubela.co/proxycurl/docs#company-api-company-profile-endpoint) with the `use_cache=if-recent` parameter.
        :type enrich_profile: str
        :return: An object of :class:`proxycurl.models.CompanyUrlEnrichResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.CompanyUrlEnrichResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if company_location is not None:
            params['company_location'] = company_location
        if company_domain is not None:
            params['company_domain'] = company_domain
        if company_name is not None:
            params['company_name'] = company_name
        if enrich_profile is not None:
            params['enrich_profile'] = enrich_profile

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/resolve',
            params=params,
            data={
            },
            result_class=CompanyUrlEnrichResult
        )

    def find_job(
        self,
        job_type: str = None,
        experience_level: str = None,
        when: str = None,
        flexibility: str = None,
        geo_id: str = None,
        keyword: str = None,
        search_id: str = None,
    ) -> JobListPage:
        """Job Search Endpoint
        
                Cost: 2 credits / successful request.
        List jobs posted by a company on LinkedIn
        
        :param job_type: The nature of the job.
            It accepts the following 7 case-insensitive values only:
            - `full-time`
            - `part-time`
            - `contract`
            - `internship`
            - `temporary`
            - `volunteer`
            - `anything` (default)
        :type job_type: str
        :param experience_level: The experience level needed for the job.
            It accepts the following 6 case-insensitive values only:
            - `internship`
            - `entry_level`
            - `associate`
            - `mid_senior_level`
            - `director`
            - `anything` (default)
        :type experience_level: str
        :param when: The time when the job is posted,
            It accepts the following case-insensitive values only:
            - `yesterday`
            - `past-week`
            - `past-month`
            - `anytime` (default)
        :type when: str
        :param flexibility: The flexibility of the job.
            It accepts the following 3 case insensitive values only:
            - `remote`
            - `on-site`
            - `hybrid`
            - `anything` (default)
        :type flexibility: str
        :param geo_id: The `geo_id` of the location to search for.
            For example, `92000000` is the `geo_id` of world wide.

            See [this article](https://nubela.co/blog/how-to-fetch-geo_id-parameter-for-the-job-api/?utm_source=blog&utm_medium=web&utm_campaign=docs-redirect-to-geo_id-article) as to how you may be able to match regions to `geo_id` input values.
        :type geo_id: str
        :param keyword: The keyword to search for.
        :type keyword: str
        :param search_id: The `search_id` of the company on LinkedIn.
            You can get the `search_id` of a LinkedIn company via
            [Company Profile API](#company-api-company-profile-endpoint).
        :type search_id: str
        :return: An object of :class:`proxycurl.models.JobListPage` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.JobListPage`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if job_type is not None:
            params['job_type'] = job_type
        if experience_level is not None:
            params['experience_level'] = experience_level
        if when is not None:
            params['when'] = when
        if flexibility is not None:
            params['flexibility'] = flexibility
        if geo_id is not None:
            params['geo_id'] = geo_id
        if keyword is not None:
            params['keyword'] = keyword
        if search_id is not None:
            params['search_id'] = search_id

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/v2/linkedin/company/job',
            params=params,
            data={
            },
            result_class=JobListPage
        )

    def job_count(
        self,
        job_type: str = None,
        experience_level: str = None,
        when: str = None,
        flexibility: str = None,
        geo_id: str = None,
        keyword: str = None,
        search_id: str = None,
    ) -> JobListCount:
        """Jobs Listing Count Endpoint
        
                Cost: 2 credits / successful request.
        Count number of jobs posted by a company on LinkedIn
        
        :param job_type: The nature of the job.
            It accepts the following 7 case-insensitive values only:
            - `full-time`
            - `part-time`
            - `contract`
            - `internship`
            - `temporary`
            - `volunteer`
            - `anything` (default)
        :type job_type: str
        :param experience_level: The experience level needed for the job.
            It accepts the following 6 case-insensitive values only:
            - `internship`
            - `entry_level`
            - `associate`
            - `mid_senior_level`
            - `director`
            - `anything` (default)
        :type experience_level: str
        :param when: The time when the job is posted,
            It accepts the following case-insensitive values only:
            - `yesterday`
            - `past-week`
            - `past-month`
            - `anytime` (default)
        :type when: str
        :param flexibility: The flexibility of the job.
            It accepts the following 3 case insensitive values only:
            - `remote`
            - `on-site`
            - `hybrid`
            - `anything` (default)
        :type flexibility: str
        :param geo_id: The `geo_id` of the location to search for.
            For example, `92000000` is the `geo_id` of world wide.

            See [this article](https://nubela.co/blog/how-to-fetch-geo_id-parameter-for-the-job-api/?utm_source=blog&utm_medium=web&utm_campaign=docs-redirect-to-geo_id-article) as to how you may be able to match regions to `geo_id` input values.
        :type geo_id: str
        :param keyword: The keyword to search for.
        :type keyword: str
        :param search_id: The `search_id` of the company on LinkedIn.
            You can get the `search_id` of a LinkedIn company via
            [Company Profile API](#company-api-company-profile-endpoint).
        :type search_id: str
        :return: An object of :class:`proxycurl.models.JobListCount` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.JobListCount`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if job_type is not None:
            params['job_type'] = job_type
        if experience_level is not None:
            params['experience_level'] = experience_level
        if when is not None:
            params['when'] = when
        if flexibility is not None:
            params['flexibility'] = flexibility
        if geo_id is not None:
            params['geo_id'] = geo_id
        if keyword is not None:
            params['keyword'] = keyword
        if search_id is not None:
            params['search_id'] = search_id

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/v2/linkedin/company/job/count',
            params=params,
            data={
            },
            result_class=JobListCount
        )

    def employee_count(
        self,
        url: str,
        use_cache: str = None,
        linkedin_employee_count: str = None,
        employment_status: str = None,
    ) -> EmployeeCount:
        """Employee Count Endpoint
        
                Cost: 1 credit / successful request.
        Get a number of total employees of a Company.

        Get an employee count of this company from various sources.
        
        :param url: URL of the LinkedIn Company Profile to target.

            URL should be in the format of `https://www.linkedin.com/company/<public_identifier>`
        :type url: str
        :param use_cache: `if-present`: The default behavior. Fetches data from LinkDB cache regardless of age of profile.

            `if-recent`: API will make a best effort to return a fresh data no older than 29 days. Costs an extra 1 credit on top of the cost of the base endpoint.
        :type use_cache: str
        :param linkedin_employee_count: Option to include a scraped employee count value from the target company's LinkedIn profile.

            Valid values are `include` and `exclude`:

            * `exclude` (default) : To exclude the scraped employee count.
            * `include` : To include the scraped employee count.

            Costs an extra `1` credit on top of the base cost of the endpoint.
        :type linkedin_employee_count: str
        :param employment_status: Parameter to tell the API to filter past or current employees.

            Valid values are `current`, `past`, and `all`:

            * `current` (default) : count current employees
            * `past` : count past employees
            * `all` : count current & past employees
        :type employment_status: str
        :return: An object of :class:`proxycurl.models.EmployeeCount` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.EmployeeCount`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['url'] = url
        if use_cache is not None:
            params['use_cache'] = use_cache
        if linkedin_employee_count is not None:
            params['linkedin_employee_count'] = linkedin_employee_count
        if employment_status is not None:
            params['employment_status'] = employment_status

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/employees/count',
            params=params,
            data={
            },
            result_class=EmployeeCount
        )

    def employee_list(
        self,
        url: str,
        country: str = None,
        enrich_profiles: str = None,
        role_search: str = None,
        page_size: str = None,
        employment_status: str = None,
        sort_by: str = None,
        resolve_numeric_id: str = None,
    ) -> EmployeeList:
        """Employee Listing Endpoint
        
                Cost: 3 credits / employee returned.
        Get a list of employees of a Company.

        This API endpoint is powered by [LinkDB](https://nubela.co/proxycurl/linkdb), our comprehensive dataset of people and company profiles.
        
        :param url: URL of the LinkedIn Company Profile to target.

            URL should be in the format of `https://www.linkedin.com/company/<public_identifier>`
        :type url: str
        :param country: Limit the result set to the country locality of the profile. For example, set the parameter of `country=us` if you only want profiles from the US. Or you can set the parameter to `country=us,sg` if you want employees from both the US and Singapore.

            This parameter accepts a comma-separated case-insensitive values of [Alpha-2 ISO3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

            Costs an extra `3` credit per result returned.
        :type country: str
        :param enrich_profiles: Get the full profile of employees instead of only their profile urls.

            Each request respond with a streaming response of profiles.

            The valid values are:

            * `skip` (default): lists employee's profile url
            * `enrich`: lists full profile of employees

            Calling this API endpoint with this parameter would add `1` credit per employee returned.
        :type enrich_profiles: str
        :param role_search: Filter employees by their title by matching the employee's title against a *regular expression*.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a **case-insensitive** regular expression.

            (The base cost of calling this API endpoint with this parameter would be `10` credits.
            Each employee matched and returned would cost `6` credits per employee returned.)
        :type role_search: str
        :param page_size: Limit the maximum results returned per API call.

            The default value of this parameter is `10`.

            Accepted values for this parameter is an integer ranging from `1` to `200000`.

            When `enrich_profiles=enrich`, this parameter accepts value ranging from `1` to `10` and the default value is `10`.
        :type page_size: str
        :param employment_status: Parameter to tell the API to return past or current employees.

            Valid values are `current`, `past`, and `all`:

            * `current` (default) : lists current employees
            * `past` : lists past employees
            * `all` : lists current & past employees
        :type employment_status: str
        :param sort_by: Sort employees by recency.

            Valid values are:
            * `recently-joined` - Sort employees by their join date. The most recent employee is on the top of the list.
            * `recently-left` - Sort employees by their departure date. The most recent employee who had just left is on the top of this list.
            * `oldest` - Returns the oldest employees first. The oldest employee who had joined this company historically is on the top of this list.
            * `none` - The default value. Do not sort.

            If this parameter is supplied with a value other than `none`, will add `50` credits to the base cost of the API endpoint regardless number of results returned. It will also add an additional cost of `10` credits per employee returned.
        :type sort_by: str
        :param resolve_numeric_id: Enable support for Company Profile URLs with numerical IDs that you most frequently fetch from Sales Navigator. 
            We achieve this by resolving numerical IDs into vanity IDs with cached company profiles from [LinkDB](https://nubela.co/proxycurl/linkdb). 
            For example, we will turn `https://www.linkedin.com/company/1234567890` to `https://www.linkedin.com/company/acme-corp` -- for which the API endpoint only supports the latter.

            This parameter accepts the following values:
            - `false` (default value) - Will not resolve numerical IDs.
            - `true` - Enable support for Company Profile URLs with numerical IDs. 
            Costs an extra `2` credit on top of the base cost of the endpoint.
        :type resolve_numeric_id: str
        :return: An object of :class:`proxycurl.models.EmployeeList` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.EmployeeList`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['url'] = url
        if country is not None:
            params['country'] = country
        if enrich_profiles is not None:
            params['enrich_profiles'] = enrich_profiles
        if role_search is not None:
            params['role_search'] = role_search
        if page_size is not None:
            params['page_size'] = page_size
        if employment_status is not None:
            params['employment_status'] = employment_status
        if sort_by is not None:
            params['sort_by'] = sort_by
        if resolve_numeric_id is not None:
            params['resolve_numeric_id'] = resolve_numeric_id

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/employees',
            params=params,
            data={
            },
            result_class=EmployeeList
        )

    def employee_search(
        self,
        keyword_regex: str,
        linkedin_company_profile_url: str,
        page_size: str = None,
        country: str = None,
        enrich_profiles: str = None,
        resolve_numeric_id: str = None,
    ) -> EmployeeList:
        """Employee Search Endpoint
        
                Cost: 10 credits / successful request.
        Search employees of a target by their job title. This API endpoint is syntactic
        sugar for the role_search parameter under the [Employee Listing Endpoint](#company-api-employee-listing-endpoint).
        This API endpoint is powered by [LinkDB](https://nubela.co/proxycurl/linkdb), our comprehensive dataset of people
        and company profiles. For a detailed comparison between this API endpoint
        and the [Role Lookup Endpoint](#people-api-role-lookup-endpoint) or the [Person Search Endpoint](#search-api-person-search-endpoint), refer to [this article](https://nubela.co/blog/what-is-the-difference-between-the-person-search-endpoint-role-lookup-endpoint-and-the-employee-search-endpoint).
        
        :param keyword_regex: Job title keyword to search for in regular expression format.

            The accepted value for this parameter is a **case-insensitive** regular expression.
        :type keyword_regex: str
        :param linkedin_company_profile_url: LinkedIn Profile URL of the target company.
        :type linkedin_company_profile_url: str
        :param page_size: Tune the maximum results returned per API call.
            The default value of this parameter is `200000`.
            Accepted values for this parameter is an integer ranging from `1` to `200000`.
            When `enrich_profiles=enrich`, this parameter accepts value ranging from `1` to `10` and the default value is `100`.
        :type page_size: str
        :param country: Limit the result set to the country locality of the profile. For example, set the parameter of `country=us` if you only want profiles from the US.

            This parameter accepts a case-insensitive [Alpha-2 ISO3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

            Costs an extra `3` credit per result returned.
        :type country: str
        :param enrich_profiles: Get the full profile of employees instead of only their profile urls.

            Each request respond with a streaming response of profiles.

            The valid values are:

            * `skip` (default): lists employee's profile url
            * `enrich`: lists full profile of employees

            Calling this API endpoint with this parameter would add `1` credit per employee returned.
        :type enrich_profiles: str
        :param resolve_numeric_id: Enable support for Company Profile URLs with numerical IDs that you most frequently fetch from Sales Navigator. 
            We achieve this by resolving numerical IDs into vanity IDs with cached company profiles from [LinkDB](https://nubela.co/proxycurl/linkdb). 
            For example, we will turn `https://www.linkedin.com/company/1234567890` to `https://www.linkedin.com/company/acme-corp` -- for which the API endpoint only supports the latter.

            This parameter accepts the following values:
            - `false` (default value) - Will not resolve numerical IDs.
            - `true` - Enable support for Company Profile URLs with numerical IDs. 
            Costs an extra `2` credit on top of the base cost of the endpoint.
        :type resolve_numeric_id: str
        :return: An object of :class:`proxycurl.models.EmployeeList` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.EmployeeList`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['keyword_regex'] = keyword_regex
        params['linkedin_company_profile_url'] = linkedin_company_profile_url
        if page_size is not None:
            params['page_size'] = page_size
        if country is not None:
            params['country'] = country
        if enrich_profiles is not None:
            params['enrich_profiles'] = enrich_profiles
        if resolve_numeric_id is not None:
            params['resolve_numeric_id'] = resolve_numeric_id

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/employee/search',
            params=params,
            data={
            },
            result_class=EmployeeList
        )

    def role_lookup(
        self,
        company_name: str,
        role: str,
        enrich_profile: str = None,
    ) -> RoleSearchEnrichedResult:
        """Role Lookup Endpoint
        
                Cost: 3 credits / successful request.
        Returns the profile of a person who most closely matches a specified role
        in a company. For instance, it can be used to identify the "CTO" of
        "Apple". The endpoint yields a single result that represents the closest
        match. For a detailed comparison between this API endpoint and the
        [Employee Search Endpoint](#company-api-employee-search-endpoint)
        or the [Person Search Endpoint](#search-api-person-search-endpoint),
        refer to [this article](
            https://nubela.co/blog/what-is-the-difference-between-the-person-search-endpoint-role-lookup-endpoint-and-the-employee-search-endpoint).
        
        :param company_name: Name of the company that you are searching for
        :type company_name: str
        :param role: Role of the profile that you are lookin up
        :type role: str
        :param enrich_profile: Enrich the result with a cached profile of the lookup result.

            The valid values are:

            * `skip` (default): do not enrich the results with cached profile data
            * `enrich`: enriches the result with cached profile data

            Calling this API endpoint with this parameter would add 1 credit.

            If you require [fresh profile data](https://nubela.co/blog/how-fresh-are-profiles-returned-by-proxycurl-api/),
            please chain this API call with the [Person Profile Endpoint](#people-api-person-profile-endpoint) with the `use_cache=if-recent` parameter.
        :type enrich_profile: str
        :return: An object of :class:`proxycurl.models.RoleSearchEnrichedResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.RoleSearchEnrichedResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['company_name'] = company_name
        params['role'] = role
        if enrich_profile is not None:
            params['enrich_profile'] = enrich_profile

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/find/company/role',
            params=params,
            data={
            },
            result_class=RoleSearchEnrichedResult
        )

    def profile_picture(
        self,
        linkedin_company_profile_url: str,
    ) -> ProfilePicture:
        """Company Profile Picture Endpoint
        
                Cost: 0 credit / successful request.
        Get the profile picture of a company.

        Profile pictures are served from cached company profiles found within [LinkDB](https://nubela.co/proxycurl/linkdb).
        If the profile does not exist within [LinkDB](https://nubela.co/proxycurl/linkdb), then the API will return a `404` status code.
        
        :param linkedin_company_profile_url: LinkedIn Profile URL of the company that you are trying to get the profile picture of.
        :type linkedin_company_profile_url: str
        :return: An object of :class:`proxycurl.models.ProfilePicture` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.ProfilePicture`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['linkedin_company_profile_url'] = linkedin_company_profile_url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/profile-picture',
            params=params,
            data={
            },
            result_class=ProfilePicture
        )


class _LinkedinSchool:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
        use_cache: str = None,
    ) -> LinkedinSchool:
        """School Profile Endpoint
        
                Cost: 1 credit / successful request.
        Get structured data of a LinkedIn School Profile
        
        :param url: URL of the LinkedIn School Profile to crawl.

            URL should be in the format of `https://www.linkedin.com/school/<public_identifier>`
        :type url: str
        :param use_cache: `if-present` The default behavior. Fetches profile from cache regardless of age of profile. If profile is not available in cache, API will attempt to source profile externally.

            `if-recent` API will make a best effort to return a fresh profile no older than 29 days.Costs an extra `1` credit on top of the cost of the base endpoint.
        :type use_cache: str
        :return: An object of :class:`proxycurl.models.LinkedinSchool` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.LinkedinSchool`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['url'] = url
        if use_cache is not None:
            params['use_cache'] = use_cache

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/school',
            params=params,
            data={
            },
            result_class=LinkedinSchool
        )

    def student_list(
        self,
        linkedin_school_url: str,
        country: str = None,
        enrich_profiles: str = None,
        search_keyword: str = None,
        page_size: str = None,
        student_status: str = None,
        sort_by: str = None,
        resolve_numeric_id: str = None,
    ) -> StudentList:
        """Student Listing Endpoint
        
                Cost: 3 credits / student returned.
        Get a list of students of a school or university.
        
        :param linkedin_school_url: URL of the LinkedIn School Profile to target.

            URL should be in the format of `https://www.linkedin.com/school/<public_identifier>`
        :type linkedin_school_url: str
        :param country: Limit the result set to the country locality of the profile. For example, set the parameter of `country=us` if you only want profiles from the US.

            This parameter accepts a case-insensitive [Alpha-2 ISO3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

            Costs an extra `3` credit per result returned.
        :type country: str
        :param enrich_profiles: Get the full profile of students instead of only their profile urls.

            Each request respond with a streaming response of profiles.

            The valid values are:

            * `skip` (default): lists student's profile url
            * `enrich`: lists full profile of students

            *Calling this API endpoint with this parameter would add `1` credit per student returned.*
        :type enrich_profiles: str
        :param search_keyword: Filter students by their major by matching the student's major against a *regular expression*.

            The default value of this parameter is `null`.

            The accepted value for this parameter is a **case-insensitive** regular expression.

            (The base cost of calling this API endpoint with this parameter would be `10` credits.
            Each student matched and returned would cost `6` credits per student returned.)
        :type search_keyword: str
        :param page_size: Limit the maximum results returned per API call.

            The default value of this parameter is `10`.

            Accepted values for this parameter is an integer ranging from `1` to `200000`.

            When `enrich_profiles=enrich`, this parameter accepts value ranging from `1` to `10` and the default value is `10`.
        :type page_size: str
        :param student_status: Parameter to tell the API to return past or current students.

            Valid values are `current`, `past`, and `all`:

            * `current` (default) : lists current students
            * `past` : lists past students
            * `all` : lists current & past students
        :type student_status: str
        :param sort_by: Sort students by matriculation or graduation dates.

            Valid values are:
            * `recently-matriculated` - Sort students by their matriculation date. Students who had had most recently started school is on the top of the list.
            * `recently-graduated` - Sort students by their graduation date. The most recently graduated student is on the top of this list.
            * `none` - The default value. Do not sort.

            If this parameter is supplied with a value other than `none`, will add `50` credits to the base cost of the API endpoint regardless number of results returned. It will also add an additional cost of `10` credits per student returned.
        :type sort_by: str
        :param resolve_numeric_id: Enable support for School Profile URLs with numerical IDs that you most frequently fetch from Sales Navigator. 
            We achieve this by resolving numerical IDs into vanity IDs with cached company profiles from [LinkDB](https://nubela.co/proxycurl/linkdb). 
            For example, we will turn `https://www.linkedin.com/school/1234567890` to `https://www.linkedin.com/school/acme-corp` -- for which the API endpoint only supports the latter.

            This parameter accepts the following values:
            - `false` (default value) - Will not resolve numerical IDs.
            - `true` - Enable support for School Profile URLs with numerical IDs. 
            Costs an extra `2` credit on top of the base cost of the endpoint.
        :type resolve_numeric_id: str
        :return: An object of :class:`proxycurl.models.StudentList` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.StudentList`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['linkedin_school_url'] = linkedin_school_url
        if country is not None:
            params['country'] = country
        if enrich_profiles is not None:
            params['enrich_profiles'] = enrich_profiles
        if search_keyword is not None:
            params['search_keyword'] = search_keyword
        if page_size is not None:
            params['page_size'] = page_size
        if student_status is not None:
            params['student_status'] = student_status
        if sort_by is not None:
            params['sort_by'] = sort_by
        if resolve_numeric_id is not None:
            params['resolve_numeric_id'] = resolve_numeric_id

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/school/students',
            params=params,
            data={
            },
            result_class=StudentList
        )


class _LinkedinJob:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
    ) -> JobProfile:
        """Job Profile Endpoint
        
                Cost: 2 credits / successful request.
        Get structured data of a LinkedIn Job Profile
        
        :param url: URL of the LinkedIn Job Profile to target.

            URL should be in the format of
            `https://www.linkedin.com/jobs/view/<job_id>`.
            [Jobs Listing Endpoint](#jobs-api-jobs-listing-endpoint)
            can be used to retrieve a job URL.
        :type url: str
        :return: An object of :class:`proxycurl.models.JobProfile` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.JobProfile`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        params['url'] = url

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/job',
            params=params,
            data={
            },
            result_class=JobProfile
        )


class _LinkedinCustomers:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def listing(
        self,
        linkedin_company_profile_url: str = None,
        twitter_profile_url: str = None,
        page_size: str = None,
    ) -> CustomerList:
        """Customer Listing Endpoint
        
                Cost: 10 credits / result for users on an annual subscription or Enterprise plan.
        Get a list of probable corporate customers of a target company.
        
        :param linkedin_company_profile_url: The LinkedIn Profile URL of the company from which you want to get a list of customers of.

            URL should be in the format of `https://www.linkedin.com/company/<public-identifier>`


            Yes (Include only one of: `linkedin_company_profile_url` or `twitter_profile_url`)
        :type linkedin_company_profile_url: str
        :param twitter_profile_url: The Twitter/X Profile URL belonging to the company that you want to get a list of customers of.

            URL should be in the format of `https://x.com/<public-identifier>`


            Yes (Include only one of: `linkedin_company_profile_url` or `twitter_profile_url`)
        :type twitter_profile_url: str
        :param page_size: Limit the maximum results of customer companies returned per API call.

            The default value of this parameter is 10.

            Accepted values for this parameter is an integer ranging from 0 to 1000.
        :type page_size: str
        :return: An object of :class:`proxycurl.models.CustomerList` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.CustomerList`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}
        if linkedin_company_profile_url is not None:
            params['linkedin_company_profile_url'] = linkedin_company_profile_url
        if twitter_profile_url is not None:
            params['twitter_profile_url'] = twitter_profile_url
        if page_size is not None:
            params['page_size'] = page_size

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/customers',
            params=params,
            data={
            },
            result_class=CustomerList
        )


class _Linkedin:
    person: _LinkedinPerson
    company: _LinkedinCompany
    school: _LinkedinSchool
    job: _LinkedinJob
    customers: _LinkedinCustomers

    def __init__(self, proxycurl):
        self.proxycurl = proxycurl
        self.person = _LinkedinPerson(self)
        self.company = _LinkedinCompany(self)
        self.school = _LinkedinSchool(self)
        self.job = _LinkedinJob(self)
        self.customers = _LinkedinCustomers(self)


class Proxycurl(ProxycurlBase):
    linkedin: _Linkedin

    def __init__(
        self,
        api_key: str = PROXYCURL_API_KEY,
        base_url: str = BASE_URL,
        timeout: int = TIMEOUT,
        max_retries: int = MAX_RETRIES,
        max_backoff_seconds: int = MAX_BACKOFF_SECONDS
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_backoff_seconds = max_backoff_seconds
        self.linkedin = _Linkedin(self)

    def get_balance(
        self,
    ) -> CreditBalance:
        """View Credit Balance Endpoint
        
                Cost: 0 credit / successful request.
        Get your current credit(s) balance
        
        :return: An object of :class:`proxycurl.models.CreditBalance` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.CreditBalance`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """
        params = {}

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/credit-balance',
            params=params,
            data={
            },
            result_class=CreditBalance
        )
