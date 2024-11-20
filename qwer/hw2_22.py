class Artist(Model):
  artist_id = AutoField(primary_key=True, column_name='ArtistId')
  name = CharField(max_length=120, column_name='Name')

  class Meta:
      database = db
      table_name = 'Artist'


class Album(Model):
  album_id = AutoField(primary_key=True, column_name='AlbumId')
  title = CharField(max_length=160, column_name='Title')
  artist = ForeignKeyField(Artist, column_name='ArtistId', backref='albums')

  class Meta:
      database = db
      table_name = 'Album'


class Customer(Model):
  customer_id = AutoField(primary_key=True, column_name='CustomerId')
  first_name = CharField(max_length=40, column_name='FirstName')
  last_name = CharField(max_length=20, column_name='LastName')
  company = CharField(max_length=80, column_name='Company', null=True)
  address = CharField(max_length=70, column_name='Address', null=True)
  city = CharField(max_length=40, column_name='City', null=True)
  state = CharField(max_length=40, column_name='State', null=True)
  country = CharField(max_length=40, column_name='Country', null=True)
  postal_code = CharField(max_length=10, column_name='PostalCode', null=True)
  phone = CharField(max_length=24, column_name='Phone', null=True)
  fax = CharField(max_length=24, column_name='Fax', null=True)
  email = CharField(max_length=60, column_name='Email')

  class Meta:
      database = db
      table_name = 'Customer'


class Employee(Model):
  employee_id = AutoField(primary_key=True, column_name='EmployeeId')
  last_name = CharField(max_length=20, column_name='LastName')
  first_name = CharField(max_length=20, column_name='FirstName')
  title = CharField(max_length=30, column_name='Title', null=True)
  reports_to = ForeignKeyField('self', column_name='ReportsTo', null=True)
  birth_date = DateField(column_name='BirthDate', null=True)
  hire_date = DateField(column_name='HireDate', null=True)
  address = CharField(max_length=70, column_name='Address', null=True)
  city = CharField(max_length=40, column_name='City', null=True)
  state = CharField(max_length=40, column_name='State', null=True)
  country = CharField(max_length=40, column_name='Country', null=True)
  postal_code = CharField(max_length=10, column_name='PostalCode', null=True)
  phone = CharField(max_length=24, column_name='Phone', null=True)
  fax = CharField(max_length=24, column_name='Fax', null=True)
  email = CharField(max_length=60, column_name='Email')

  class Meta:
      database = db
      table_name = 'Employee'


class Genre(Model):
  genre_id = AutoField(primary_key=True, column_name='GenreId')
  name = CharField(max_length=120, column_name='Name')

  class Meta:
      database = db
      table_name = 'Genre'


class MediaType(Model):
  media_type_id = AutoField(primary_key=True, column_name='MediaTypeId')
  name = CharField(max_length=120, column_name='Name')

  class Meta:
      database = db
      table_name = 'MediaType'


class Playlist(Model):
  playlist_id = AutoField(primary_key=True, column_name='PlaylistId')
  name = CharField(max_length=120, column_name='Name')

  class Meta:
      database = db
      table_name = 'Playlist'


class PlaylistTrack(Model):
  playlist = ForeignKeyField(Playlist, column_name='PlaylistId', backref='playlist_tracks')
  track = ForeignKeyField(Track, column_name='TrackId', backref='playlist_tracks')

  class Meta:
      database = db
      table_name = 'PlaylistTrack'


class Track(Model):
  track_id = AutoField(primary_key=True, column_name='TrackId')
  name = CharField(max_length=200, column_name='Name')
  album = ForeignKeyField(Album, column_name='AlbumId', backref='tracks')
  media_type = ForeignKeyField(MediaType, column_name='MediaTypeId', backref='tracks')
  genre = ForeignKeyField(Genre, column_name='GenreId', backref='tracks', null=True)
  composer = CharField(max_length=220, column_name='Composer', null=True)
  milliseconds = IntegerField(column_name='Milliseconds')
  bytes = IntegerField(column_name='Bytes', null=True)
  unit_price = DecimalField(max_digits=10, decimal_places=2, column_name='UnitPrice')

  class Meta:
      database = db
      table_name = 'Track'


class Invoice(Model):
  invoice_id = AutoField(primary_key=True, column_name='InvoiceId')
  customer = ForeignKeyField(Customer, column_name='CustomerId', backref='invoices')
  invoice_date = DateTimeField(column_name='InvoiceDate')
  billing_address = CharField(max_length=70, column_name='BillingAddress')
  billing_city = CharField(max_length=40, column_name='BillingCity')
  billing_state = CharField(max_length=40, column_name='BillingState')
  billing_country = CharField(max_length=40, column_name='BillingCountry')
  billing_postal_code = CharField(max_length=10, column_name='BillingPostalCode')
  total = DecimalField(max_digits=10, decimal_places=2, column_name='Total')

  class Meta:
      database = db
      table_name = 'Invoice'


class InvoiceLine(Model):
  invoice_line_id = AutoField(primary_key=True, column_name='InvoiceLineId')
  invoice = ForeignKeyField(Invoice, column_name='InvoiceId', backref='invoice_lines')
  track = ForeignKeyField(Track, column_name='TrackId', backref='invoice_lines')
  unit_price = DecimalField(max_digits=10, decimal_places=2, column_name='UnitPrice')
  quantity = IntegerField(column_name='Quantity')

  class Meta:
      database = db
      table_name = 'InvoiceLine'