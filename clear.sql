
DROP SCHEMA public CASCADE;

CREATE SCHEMA public
  AUTHORIZATION blog;

GRANT ALL ON SCHEMA public TO blog;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public
  IS 'standard public schema';