class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str):
            raise TypeError('Names must be of type str')
        if len(name) == 0:
            raise ValueError('The name must be greater than zero')
        if not isinstance(hometown, str):
            raise TypeError('Hometown should be of type str!')
        if len(hometown) == 0:
            raise ValueError('Hometown should be greater than zero')

        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('The name must be a string')
        if len(value) == 0:
            raise ValueError('The name cannot be empty')
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return self._concerts
    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for concert in self.concerts()]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self._date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
        band._concerts.append(self)
        venue._concerts.append(self)   

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('date must be a string!')
        if len(value) == 0:
            raise ValueError("The date can't be empty!")
        self._date = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise TypeError('The venue must be of type Venue')
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    @property
    def band(self):
        return self._band
    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise TypeError('The band must be of type Band')
        self._band = value

class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string!')
        self._name = value
        if len(value) == 0:
            raise ValueError('The number should be greater than 0!')

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise TypeError('cities must be strings!')
        self._city = value
        if len(value) == 0:
            raise ValueError('cities are longer than 0 characters')
    def concerts(self):
        return self._concerts

    def bands(self):
        my_unique_bands = set(concert.band for concert in self._concerts)
        return list(my_unique_bands)