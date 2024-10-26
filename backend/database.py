from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URI: Use SQLite by default, but PostgreSQL can be configured.
DATABASE_URL = "sqlite:///rules.db"  # For SQLite
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost/rules_db"  # For PostgreSQL

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Define a base class for declarative class definitions
Base = declarative_base()

# Define a Rule model for the rules table
class Rule(Base):
    __tablename__ = "rules"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    rule_expression = Column(Text, nullable=False)  # Store the rule as a string expression

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)

# CRUD operations
def add_rule(name: str, rule_expression: str):
    """Add a new rule to the database."""
    session = SessionLocal()
    try:
        new_rule = Rule(name=name, rule_expression=rule_expression)
        session.add(new_rule)
        session.commit()
        print(f"Rule '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Failed to add rule: {e}")
    finally:
        session.close()

def get_rule(name: str):
    """Retrieve a rule by name."""
    session = SessionLocal()
    try:
        rule = session.query(Rule).filter(Rule.name == name).first()
        return rule
    finally:
        session.close()

def update_rule(name: str, new_expression: str):
    """Update an existing rule's expression."""
    session = SessionLocal()
    try:
        rule = session.query(Rule).filter(Rule.name == name).first()
        if rule:
            rule.rule_expression = new_expression
            session.commit()
            print(f"Rule '{name}' updated successfully.")
        else:
            print(f"Rule '{name}' not found.")
    except Exception as e:
        session.rollback()
        print(f"Failed to update rule: {e}")
    finally:
        session.close()

def delete_rule(name: str):
    """Delete a rule by name."""
    session = SessionLocal()
    try:
        rule = session.query(Rule).filter(Rule.name == name).first()
        if rule:
            session.delete(rule)
            session.commit()
            print(f"Rule '{name}' deleted successfully.")
        else:
            print(f"Rule '{name}' not found.")
    except Exception as e:
        session.rollback()
        print(f"Failed to delete rule: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # Initialize the database
    init_db()
    # Example usage:
    # add_rule("rule1", "age > 30 AND department = 'Sales'")
    # rule = get_rule("rule1")
    # print(f"Retrieved Rule: {rule.name}, Expression: {rule.rule_expression}")
