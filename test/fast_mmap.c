#include<sys/mman.h>
#include<errno.h>
#include<string.h>
#include<stdlib.h>

typedef struct fmmap_st {
	void *ptr;
	size_t length;
} fmmap_st;

int fmmap_mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset, fmmap_st *mm){
	void *ptr;
	ptr = mmap(addr, length, prot, flags, fd, offset);
	if (!ptr){
	    return -1;
	}
	*mm = (fmmap_st){ptr, length};
	return 0;
}

int fmmap_unmap(fmmap_st mm){
	return munmap(mm.ptr, mm.length);
}

int fmmap_write(fmmap_st mm, void *data, size_t start, size_t length){
	if(start+length>mm.length){
		errno = EFAULT;
		return -1;
	}
	memcpy(mm.ptr+start,data,length);
	return 0;
}

char *fmmap_read(fmmap_st mm, size_t start, size_t length){
	if(start+length>mm.length){
		errno = EFAULT;
		return NULL;
	}
	char *out=malloc(length*sizeof(char));
	memcpy(out, mm.ptr+start, length);
	return out;
}

void *fmmap_getptr(fmmap_st mm, size_t start){
	if(start>mm.length){
		errno=EFAULT;
		return NULL;
	}
	return mm.ptr+start;
}

int fmmap_sync(fmmap_st mm, int flags) {
    return msync(mm.ptr, mm.length, flags);
}

