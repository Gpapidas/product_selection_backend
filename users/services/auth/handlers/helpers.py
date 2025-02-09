def initialize_user_session(session):
    """
    Initializes session storage for search queries and product selection.
    """
    session["last_search_query"] = ""
    session["selected_products"] = []
    session.modified = True


def clear_user_session(session):
    """
    Clears session data completely.
    """
    session.flush()
