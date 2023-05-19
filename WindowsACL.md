
|Permission||
|----------|---------------|
|`full_set`|all permissions|
|`modify_set`|all permissions except write_acl and write_owner|
|`read_set`|read_data, read_attributes, read_xattr and read_acl|
|`write_set`|write_data, append_data, write_attributes and write_xattr|


            owner@:--------------:-------:deny
            owner@:rwxp---A-W-Co-:-------:allow
            group@:-w-p----------:-------:deny
            group@:r-x-----------:-------:allow
         everyone@:-w-p---A-W-Co-:-------:deny
         everyone@:r-x---a-R-c--s:-------:allow
                   ||||||||||||||:|||||||
      (r)read data +|||||||||||||:||||||+ (I)nherited
      (w)rite data -+||||||||||||:|||||+- (F)ailed access (audit)
         e(x)ecute --+|||||||||||:||||+-- (S)uccess access (audit)
          a(p)pend ---+||||||||||:|||+--- (n)o propagate
          (d)elete ----+|||||||||:||+---- (i)nherit only
    (D)elete child -----+||||||||:|+----- (d)irectory inherit
     read (a)ttrib ------+|||||||:+------ (f)ile inherit
    write (A)ttrib -------+||||||
      (R)ead xattr --------+|||||
     (W)rite xattr ---------+||||
        read a(c)l ----------+|||
       write a(C)l -----------+||
    change (o)wner ------------+|
              sync -------------+

Windows ACL to show files but not let them be opened:

First ACL (this first ACL is the same as "List Folder Contents")

* Apply to: This folder and subfolders (read the drop down carefully here)
* Allows:
  * Traverse folder/execute file
  * List folder/read data
  * Read attributes
  * Read extended attributes
  * Read permissions

Second ACL:

* Apply to: Files only
* Allows:
  * Read attributes
  * Read extended attributes
  * Read permissions

Select "Replace all child object permission entries..."

Alternatively, in the terminal:
* `setfacl -m everyone@:r-x---a-R-c---:-d-----:allow myFolder`
* `setfacl -a 0 everyone@:------a-R-c---:f-i----:allow myFolder`



## More examples
    getfacl myFolder

    setfacl -m owner@:rwxpDdaARWcCo-:fd-----:allow folder
    setfacl -m u:someuser:full_set:allow folder
    find /mnt/ZFS1/test/ -type f -exec setfacl -m u:John:modify_set:allow {} \;

    setfacl -b removes an acl entry. You can use also use the -R flag for recursion.

Make a folder and fine tune setting in windows (e.g. remove `everyone`)

   mkdir folder
   chown -R someUser folder
   chgrp -R someGroup folder
   setfacl -m owner@:full_set:allow folder
   setfacl -m group@:full_set:allow folder


## Relevant
* https://forums.freenas.org/index.php?threads/setfacl-recursive-quick-and-dirty-how.16146/
* http://www.shrubbery.net/solaris9ab/SUNWaadm/SYSADV6/p50.html
