import { TestBed } from '@angular/core/testing';

import { Nome } from './nome';

describe('Nome', () => {
  let service: Nome;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Nome);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
