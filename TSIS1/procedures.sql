CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phones(phone) VALUES (p_phone);
END;
$$;

CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO groups(name) VALUES (p_group);
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(q TEXT)
RETURNS TABLE(name TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT name FROM contacts WHERE name ILIKE '%' || q || '%';
END;
$$;