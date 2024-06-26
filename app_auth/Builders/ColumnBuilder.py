class ColumnBuilder:
    def __init__(self, request):
        self.request = request;
        self.baseQuery().attachColumnType().attachPrimaryKey().attachNullable().attachDefault().attachForeignKey();

    def get(self):
        return self.query;

    def baseQuery(self):
        # Update column
        if (self.request.POST.get('old_name') != ''):
            self.is_create = False;

            self.query = "ALTER TABLE {} MODIFY COLUMN {}".format(
                self.request.POST.get('table'),
                self.request.POST.get('old_name'),
            );

            return self;

        # Create column
        self.query = "ALTER TABLE {} ADD COLUMN {}".format(
            self.request.POST.get('table'),
            self.request.POST.get('name')
        );

        self.is_create = True;

        return self;

    def attachColumnType(self):
        match self.request.POST.get('type'):
            case 'CHAR' | 'VARCHAR' | 'BINARY' | 'VARBINARY' | 'TEXT' | 'BLOB' | 'LONGTEXT' | 'TINYTEXT' | 'MEDIUMTEXT' | 'BIT':
                self.query += " {}({})".format(self.request.POST.get('type'), self.request.POST.get('max_length'));
            case 'SET' | 'ENUM':
                self.query += " {}({})".format(self.request.POST.get('type'),
                                               ",".join(str("'{}'".format(x)) for x in self.request.POST.getlist('options')))
            case _:
                self.query += " {}".format(self.request.POST.get('type'));

        return self;

    def attachNullable(self):
        if self.request.POST.get('nullable') == '0':
            self.query += " NOT NULL";

        return self;

    def attachDefault(self):
        if self.request.POST.get('default') != None and self.request.POST.get('default') != '':
            self.query += " DEFAULT {}".format(self.request.POST.get('default'));

        return self;

    def attachPrimaryKey(self):
        if self.request.POST.get('pk') == '1' and self.request.POST.get('old_pk') != '1':
            self.query += " PRIMARY KEY";

        return self;

    def attachForeignKey(self):
        if self.request.POST.get('fk') == '1' and self.request.POST.get(
            'fk_table') != '' and self.request.POST.get('fk_column') != '':
            self.query += ", ADD CONSTRAINT FOREIGN KEY (`{}`) REFERENCES {}(`{}`);".format(
                self.request.POST.get('name') if self.is_create else self.request.POST.get('old_name'),
                self.request.POST.get('fk_table'),
                self.request.POST.get('fk_column')).upper()

        return self;
