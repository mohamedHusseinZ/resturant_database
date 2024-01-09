from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Restaurant(Base):
    # define Restaurant table name
    __tablename__ = 'restaurants'

    # create class attributes and table columns
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # create class relationships as attributes
    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer')

    # represent the class instances
    def __repr__(self):
        return f'{self.name} Restaurant - Price: ${self.price}.00\n'

    # return details of all the restaurant instance reviews
    def all_reviews(self):
        return [
            f'Review for {self.name} by {session.query(Customer).filter(Customer.id == review.customer_id).first().full_name}: {review.star_rating}stars.'
            for review in self.reviews]


    # return all the restaurant instance reviews
    @property
    def restaurant_reviews(self):
        return self.reviews

    # return all the customers who have reviewed this restaurant
    @property
    def restaurant_customers(self):
        return self.customers

    # returns the fanciest(most-expensive) restaurant of all the restaurants
    @classmethod
    def fanciest_restaurant(cls):
        all_restaurants = session.query(cls).all()
        return f'The fanciest restaurant is {max(all_restaurants, key=lambda restaurant: restaurant.price)}.'



class Customer(Base):
    # define Restaurant table name
    __tablename__ = 'customers'

    # create class attributes and table columns
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # create class relationships as attributes
    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant')

    # represent the class instances
    def __repr__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}\n'

    # returns the customer reviews
    @property
    def customer_reviews(self):
        return self.reviews

    # returns the customer reviews
    @property
    def customer_restaurants(self):
        return self.restaurants